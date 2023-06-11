using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class LanaguageControl : MonoBehaviour
{
    public Dropdown dropdown;
    private string gamelang;
    private void Start()
    {
        gamelang = PlayerPrefs.GetString("gamelang");
        Debug.Log(gamelang);
        if (gamelang == "en")
        {
            dropdown.value = 0;
        }
        else if (gamelang == "zh")
        {
            dropdown.value = 1;
        }
        else if (gamelang == "es")
        {
            dropdown.value = 2;
        }
        else if (gamelang == "it")
        {
            dropdown.value = 3;
        }
        //dropdown = this.gameObject.GetComponent<Dropdown>();
    }
    private void Update()
    {
        if (dropdown.value == 0)
        {
            PlayerPrefs.SetString("gamelang", "en");
            //Debug.Log("Language:" + I18n.Get2LetterISOCodeFromSystemLanguage());
        }
        else if (dropdown.value == 1)
        {
            PlayerPrefs.SetString("gamelang", "zh");
            //Debug.Log("Language:" + I18n.Get2LetterISOCodeFromSystemLanguage());
        }
        else if (dropdown.value == 2)
        {
            PlayerPrefs.SetString("gamelang", "es");
            //Debug.Log("Language:" + I18n.Get2LetterISOCodeFromSystemLanguage());
        }
        else if (dropdown.value == 3)
        {
            PlayerPrefs.SetString("gamelang", "it");
            //Debug.Log("Language:" + I18n.Get2LetterISOCodeFromSystemLanguage());
        }
    }

    public void RestartScene()
    {
        SceneManager.LoadScene("StartScreen");
    }
}
