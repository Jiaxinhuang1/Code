using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Audio;

public class MusicController : MonoBehaviour
{
    //This script is attached to an empty volume controller gameobject to control the volume and sound effects slider

    //variable so the volume mixer still applies even if slider is not active
    public AudioMixer mixer;
    public AudioMixer effectsMixer;
    public Slider volumeSlider;
    public Slider effectsSlider;

    // Start is called before the first frame update
    void Start()
    {
        //Start by getting the saved volume from the previous setup
        // If first time, set default to 1
        volumeSlider.value = PlayerPrefs.GetFloat("MusicVolume", 1f);
        effectsSlider.value = PlayerPrefs.GetFloat("EffectsVolume", 1f);
    }

    // function called whenever the volume slider value is changed
    public void SetLevel()
    {
        // Set the mixer volume based on slider value and save
        float volumeValue = volumeSlider.value;
        mixer.SetFloat("MusicVolume", Mathf.Log10(volumeValue) * 20);
        PlayerPrefs.SetFloat("MusicVolume", volumeValue);

    }
    // function called whenever the sound effecs slider volume is changed
    public void SetEffectsLevel()
    {
        // sound effects slider
        float effectsValue = effectsSlider.value;
        effectsMixer.SetFloat("MusicVolume", Mathf.Log10(effectsValue) * 20);
        PlayerPrefs.SetFloat("EffectsVolume", effectsValue);
    }
}
