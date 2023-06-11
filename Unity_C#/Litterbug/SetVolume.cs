using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Audio;
using UnityEngine.UI;

public class SetVolume : MonoBehaviour
{
    //variable so the volume mixer still applies even if slider is not active
    public AudioMixer mixer;
    public Slider volumeSlider;

    // Start is called before the first frame update
    void Start()
    {
        //Start by getting the saved volume from the previous setup
        // If first time, set default to 0.75
        volumeSlider.value = PlayerPrefs.GetFloat("MusicVolume", 0.75f);
    }

    public void SetLevel()
    {
        // Set the mixer volume based on slider value and save
        float sliderValue = volumeSlider.value;
        mixer.SetFloat("MusicVolume", Mathf.Log10(sliderValue) * 20);
        PlayerPrefs.SetFloat("MusicVolume", sliderValue);
    }
}
