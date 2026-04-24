---
title: SSML Tags
summary: Programmable voice with SSML tags from Telnyx - perfect for your next conference call, voicemail greeting, or even a singing telegram!.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/ssml-tags/index
    content_hash: 13dc4d8c806693c8719395efacc840f60419e80f0be295dc6b2fdea869fc8a1b
updated_at: 2026-04-10T00:00:00Z
---

# SSML Tags

Programmable voice with SSML tags from Telnyx - perfect for your next conference call, voicemail greeting, or even a singing telegram!

In this tutorial, you'll learn about SSML tags that can help customize your audio response in your text-to-speech application.

This tutorial assumes you've already [set up your developer account and environment](/development) and you know how to [send commands](sending-commands-for-programmable-voice.md) and [receive webhooks](receiving-webhooks-for-programmable-voice.md) using the Telnyx Voice API.

## What are SSML tags?

Speech Synthesis Markup Language (SSML) is an XML-based markup language that is used to generate synthetic speech for appliations. SSML tags are used to change the tone of speech in the application by adjusting pitching, volume, duration of speech, and more.

## SSML tag examples

### Adding a pause

**SSML Tag:**

`<break> </break>`

There are 2 ways for defining the length of the pause by using the following attributes:

1. Time: Defines the number of s or ms
2. Strength: Chooses the strength using the following values:

* None: no pause
* Pause: the same duration as after a period
* x-weak: the same as none.
* weak: sets a pause of the same duration as the pause after a comma
* medium: has the same strength as weak
* strong: sets a pause of the same duration as the pause after a sentence
* x-strong: sets a pause of the same duration as the pause after a paragraph.

**Example:**

```
<speak> Mary had a little lamb <break time="3s"/>Whose fleece was white as snow. </speak>
```

### Emphasizing words

**SSML Tag:**

```
<emphasis> </emphasis>
```

The emphasising affects the speed and loudness of reading words and can be defined by using a 'level' attribute with one of the following values:

1. Strong - increases the volume and slows the speaking rate
2. Moderate - increases the volume and slows the speaking rate, but less than Strong
3. Reduced - decreases the volume and speeds up the speaking rate

**Example:**

```
<speak> I already told you we're <emphasis level="strong">nearly</emphasis> there </speak>
```

### Set a different language

**SSML Tag:**

```
<lang> </lang>
```

The **xml:lang** tag defines the language for a specific word or sentence.

\_\_Example: \_\_

```
<speak> <xml:lang=”es”>Puedo hablar español</xml:lang=”es”> </speak>
```

### Adding a pause between paragraphs

**SSML Tag:**

```
<p> </p>
```

This tag adds a pause between paragraphs that is longer than a regular pause at a comma or at the end of the sentence.

**Example:**

```
<speak>
<p>This is the first paragraph.</p> <p>This is the second paragraph.</p>
</speak>
```

### Using phonetic pronunciation

**SSML Tag:**

```
<phoneme> </phoneme>
```

The phonetic pronunciation requires 2 attributes:

1. **Alphabet**, with the following options:

* ipa, meaning the International Phonetic Alphabet (IPA) will be used
* x-sampa, which indicates that the Extended Speech Assessment Methods Phonetic Alphabet (X-SAMPA) will be used.

2. **ph**, specifies how the text should be pronounced.

**Example:**

```
<speak>Say <phoneme alphabet="ipa" ph="prəˌnʌnsɪˈeɪʃ(ə)n">pronunciation</phoneme>. </speak>
```

### Controlling volume, speaking rate, and pitch

**SSML Tag:**:

```
<prosody> </prosody>
```

The following attributes can be used with the Prosody tag:

1. **Volume**:

* default: resets the volume to default value
* silent, x-soft, soft, medium, loud, x-loud: sets the volume to predefined     value
* +ndB, -ndB: changes the volume relative to the current level

2. **Rate**:

* x-slow, slow, medium, fast,x-fast: sets the pitch to a predefined value
* n%: a percentage change in speaking pace.

**Exmaple:**

```
<speak>
Sometimes some words need to be said <prosody volume=”loud>louder</prosody> and sometimes a lower volume <prosody volume="-6dB">is a more effective way of interacting with your audience. </prosody> 
</speak>
```

### Adding a pause between sentences

**SSML Tag:**

```
<s> </s>
```

This tag adds a pause between lines with the same effect as (.)

**Example:**

```
<speak>
<s>Here we go round the mulberry bush</s>
<s>On a cold and frosty morning</s>
</speak>
```

### Controlling how special words are spoken

**SSML Tags:**

```
<say-as> </say-as>
```

The say-as tag uses one attribute,'interpret-as', which uses a number of possible available values:

* characters or spell-out
* cardinal or number
* digits
* fraction
* unit
* date
* time
* address
* telephone.

**Example:**

```
<speak><say-as interpret-as=”telephone”>+19999999</say-as></speak> 
```

### Pronouncing acronyms and abbreviations

**SSML Tag:**

```
<sub> </sub>
```

This tag should be used with the alias attribute to substitute a different word for selected text such as an acronym or abbreviation.

**Example:**

```
<speak> My favorite chemical element is <sub alias="Mercury">Hg</sub>, because it looks so shiny. </speak>
```
