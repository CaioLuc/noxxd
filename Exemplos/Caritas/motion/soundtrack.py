"""Trilha de 50 s do vídeo CARITAS, sintetizada do zero (sem samples, sem licença de terceiros).

120 BPM, Ré maior. Os tempos dos efeitos espelham as deixas de index.html.
Uso: python soundtrack.py  -> soundtrack.wav (44,1 kHz, estéreo, 16 bits)
"""
import wave
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve

SR, DUR, BPM = 44100, 50.0, 120
N = int(SR * DUR)
BEAT = 60 / BPM
rng = np.random.default_rng(7)
L = np.zeros(N); R = np.zeros(N)          # bus seco
WL = np.zeros(N); WR = np.zeros(N)        # envio de reverb
KL = np.zeros(N)                           # bumbo, fora do sidechain


def midi(m): return 440 * 2 ** ((m - 69) / 12)
def tt(d): return np.arange(int(d * SR)) / SR
def filt(x, kind, f, order=2): return sosfilt(butter(order, f, kind, fs=SR, output='sos'), x)


def add(sig, at, gain=1.0, pan=0.0, wet=0.0, bus=None):
    i = int(at * SR)
    if i >= N: return
    sig = sig[:N - i] * gain
    if bus is not None:
        bus[i:i + len(sig)] += sig; return
    gl, gr = np.sqrt((1 - pan) / 2), np.sqrt((1 + pan) / 2)
    L[i:i + len(sig)] += sig * gl; R[i:i + len(sig)] += sig * gr
    if wet:
        WL[i:i + len(sig)] += sig * gl * wet; WR[i:i + len(sig)] += sig * gr * wet


def env(n, a, d):  # ataque linear, decaimento exponencial
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)


def saw(f, t, detune=(0, -7, 7)):
    return sum(2 * ((f * 2 ** (c / 1200) * t + rng.random()) % 1) - 1 for c in detune) / len(detune)


# ---------- harmonia ----------
CHORDS = {'D': [50, 57, 61, 64, 66], 'Bm': [47, 54, 57, 62, 66], 'G': [43, 50, 54, 59, 62], 'A': [45, 52, 57, 61, 64]}
PROG = ['D', 'Bm', 'G', 'A']
def chord_at(t):
    if t >= 46: return 'D' if t >= 48 else 'A'
    return PROG[int(t // 4) % 4]


# ---------- pad (do início ao fim) ----------
def pad(start, dur, notes, cutoff, gain):
    t = tt(dur + 1.5)
    x = sum(saw(midi(m), t) for m in notes) / len(notes)
    x = filt(x, 'lowpass', cutoff)
    e = np.minimum(1, t / 0.6) * np.clip((dur + 1.5 - t) / 1.5, 0, 1)
    add(x * e, start, gain, pan=0, wet=0.6)
    add(np.roll(x, 300) * e, start, gain * .5, pan=.6)

for k in range(13):
    s = k * 4.0
    name = chord_at(s + .01)
    cut = 700 if s < 10 else (1500 if s < 41 else 900)
    pad(s, 4.0, CHORDS[name], cut, .22 if s < 10 else .17)

# ---------- percussão ----------
def kick():
    t = tt(.45); f = 45 + 95 * np.exp(-t / .045)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / .16) + rng.normal(0, 1, len(t)) * np.exp(-t / .004) * .3
def clap():
    t = tt(.3); n = filt(rng.normal(0, 1, len(t)), 'bandpass', [900, 3200])
    e = sum(np.exp(-np.maximum(t - o, 0) / .012) * (t >= o) for o in (0, .011, .022)) / 2 + np.exp(-t / .12) * .6
    return n * e
def hat(d=.045): t = tt(d); return filt(rng.normal(0, 1, len(t)), 'highpass', 7000) * np.exp(-t / (d / 3))

K, C = kick(), clap()
duck = np.ones(N)
for b in np.arange(0, DUR, BEAT):
    full = 10 <= b < 41 or 46 <= b < 47.4
    half = 41 <= b < 45.5 and round((b - 41) / BEAT) % 2 == 0
    if full or half:
        add(K, b, .9, bus=KL)
        i = int(b * SR); n = min(int(.25 * SR), N - i)
        duck[i:i + n] = np.minimum(duck[i:i + n], 1 - .55 * np.exp(-np.arange(n) / SR / .09))
    if full and round(b / BEAT) % 2 == 1: add(C, b, .35, wet=.4)
for s in np.arange(6, 41, BEAT / 2):
    off = round(s / (BEAT / 2)) % 2 == 1
    if (6 <= s < 10 and off) or (10 <= s < 24 and off): add(hat(), s, .16, pan=.3)
for s in np.arange(24, 41, BEAT / 4): add(hat(.03), s, .09 if round(s / (BEAT / 4)) % 2 else .14, pan=-.25)

# ---------- baixo (colcheias) e arpejo (semicolcheias) ----------
mus_l = np.zeros(N); mus_r = np.zeros(N)
def tone(f, d, shape='bass'):
    t = tt(d)
    if shape == 'bass':
        return (np.sin(2 * np.pi * f * t) + .3 * filt(saw(f, t, (0,)), 'lowpass', 500)) * env(len(t), .005, d * .5)
    x = filt(saw(f, t, (0, 5)), 'lowpass', 2600) * .6 + np.sin(2 * np.pi * f * t) * .5
    return x * env(len(t), .003, .12)

for s in np.arange(10, 41, BEAT / 2):
    add(tone(midi(CHORDS[chord_at(s)][0] - 12 + (12 if round(s / (BEAT / 2)) % 4 == 3 else 0)), BEAT / 2), s, .38)
arp_pat = [0, 2, 3, 4, 3, 2, 1, 2]
for j, s in enumerate(np.arange(18, 41, BEAT / 4)):
    notes = CHORDS[chord_at(s)]
    add(tone(midi(notes[arp_pat[j % 8]] + 12), .3, 'pluck'), s, .10, pan=(.4 if j % 2 else -.4), wet=.5)

# ---------- efeitos ----------
def whoosh(d=.6, up=True):
    t = tt(d); n = rng.normal(0, 1, len(t))
    lo, hi = filt(n, 'bandpass', [300, 1200]), filt(n, 'bandpass', [1500, 6000])
    mix = t / d if up else 1 - t / d
    return (lo * (1 - mix) + hi * mix) * np.sin(np.pi * t / d) ** 2
def pop(f=900, d=.07):
    t = tt(d); fr = f * (1 + .6 * np.exp(-t / .01))
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * env(len(t), .001, d / 4)
def click(): t = tt(.012); return filt(rng.normal(0, 1, len(t)), 'bandpass', [2000, 6000]) * np.exp(-t / .003)
def thock(): t = tt(.12); return (np.sin(2 * np.pi * 160 * t) * .8 + filt(rng.normal(0, 1, len(t)), 'lowpass', 2500) * .4) * env(len(t), .001, .03)
def bell(m, d=1.2):
    t = tt(d); f = midi(m)
    return (np.sin(2 * np.pi * f * t) + .35 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t / .2)) * env(len(t), .002, d / 3)
def chime(m0=74, m1=81, at=0): add(bell(m0, .8), at, .16, wet=.5); add(bell(m1, 1.0), at + .09, .16, wet=.5)
def impact(d=2.5):
    t = tt(d); sub = np.sin(2 * np.pi * (38 + 40 * np.exp(-t / .1)) * t) * np.exp(-t / .7)
    return sub + filt(rng.normal(0, 1, len(t)), 'lowpass', 1800) * np.exp(-t / .25) * .35
def riser(d):
    t = tt(d); n = filt(rng.normal(0, 1, len(t)), 'highpass', 800)
    f = 200 * 2 ** (3 * t / d)
    return (n * .5 + np.sin(2 * np.pi * np.cumsum(f) / SR) * .25) * (t / d) ** 2.2

# transições
for at in [5.5, 8.75, 9.6, 17.6, 23.6, 29.6, 30.3, 34.35, 36.3, 38.5, 40.8, 45.55, 47.4]:
    add(whoosh(.7), at - .15, .22, pan=rng.uniform(-.5, .5), wet=.4)
for i in range(6): add(whoosh(.5), 6.0 + i * .1, .08, pan=(-.7 if i % 2 else .7))
add(riser(1.3), .2, .25, wet=.5); add(impact(), 1.5, .55, wet=.3)
add(riser(2.4), 7.6, .3, wet=.4); add(impact(), 10.0, .6, wet=.3)
add(riser(1.2), 47.0, .3, wet=.5); add(impact(3), 48.2, .65, wet=.4)

# letras CARITAS: sinos subindo o acorde
for i, m in enumerate([62, 66, 69, 73, 74, 78, 81]):
    add(bell(m + 12), 2.4 + i * .07, .10, pan=-.6 + i * .2, wet=.6)
    add(bell(m + 12), 48.5 + i * .05, .10, pan=-.6 + i * .2, wet=.6)

pops = ([10.85 + i * .1 for i in range(3)] + [11.45 + i * .09 for i in range(5)] + [13.75 + i * .08 for i in range(4)] +
        [19.2 + i * .17 for i in range(6)] + [21.07 + i * .07 for i in range(7)] + [24.7 + i * .15 for i in range(8)] +
        [25.2 + i * .12 for i in range(3)] + [30.35 + i * .15 for i in range(5)] + [31.6 + i * .12 for i in range(5)] +
        [35.3 + i * .065 for i in range(13)] + [36.85 + i * .07 for i in range(4)] + [42.35 + i * .15 for i in range(6)])
for i, at in enumerate(pops): add(pop(700 + (i * 137) % 600), at, .13, pan=rng.uniform(-.4, .4))
for i in range(7): add(pop(900 + i * 90, .09), 18.75 + i * .55, .15, wet=.3)   # etapas da anamnese
for at in [12.35, 12.5, 21.0, 21.15]: add(thock(), at, .35)
for at in [12.8, 21.4, 14.9, 26.45, 37.3, 37.65, 39.7]: add(click(), at, .5); add(pop(500, .05), at, .12)
for at, ms in [(13.0, (69, 76)), (15.9, (74, 78)), (21.9, (74, 81)), (37.9, (76, 83)), (38.1, (81, 86)), (40.3, (74, 86))]:
    chime(*ms, at=at)
add(impact(.6) * .6, 32.5, .5); add(thock(), 32.5, .5)                            # carimbo
for i in range(9): add(bell(86 + [0, 4, 7, 12, 7, 4, 12, 16, 19][i], .6), 26.6 + i * .07, .06, pan=rng.uniform(-.7, .7), wet=.7)
for at in rng.uniform(38.75, 39.65, 40): add(click(), at, .12, pan=rng.uniform(-.6, .6))   # QR montando
for at in np.arange(46.05, 47.15, .06): add(pop(1200 + (at - 46) * 900, .04), at, .05)     # contador 4,55

# digitação
for st, cps, n in [(13.3, 9, 3), (18.85, 44, 92), (24.65, 74, 121), (27.2, 96, 206)]:
    step = 1 if cps < 60 else 2
    for c in range(0, n, step): add(click(), st + c / cps + rng.uniform(0, .008), rng.uniform(.06, .12), pan=.2)

# acorde final
pad(48.2, 1.6, CHORDS['D'] + [69, 74], 2200, .2)

# ---------- mix ----------
ir_t = tt(2.4); ir = rng.normal(0, 1, (2, len(ir_t))) * np.exp(-ir_t / .55); ir = filt(ir, 'lowpass', 6000) / 30
wl = fftconvolve(WL, ir[0])[:N]; wr = fftconvolve(WR, ir[1])[:N]
out = np.stack([L + wl, R + wr]) * duck ** .5 + KL
out = filt(out, 'highpass', 28)
fade = np.ones(N); fl = int(1.2 * SR); fade[-fl:] = np.linspace(1, 0, fl) ** 2
fade[:int(.05 * SR)] = np.linspace(0, 1, int(.05 * SR))
out = np.tanh(out * 1.2) * fade
out = out / np.abs(out).max() * 10 ** (-1 / 20)

with wave.open('soundtrack.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((out.T * 32767).astype('<i2').tobytes())
assert abs(N / SR - DUR) < 1e-6
print('ok soundtrack.wav', round(N / SR, 2), 's')
