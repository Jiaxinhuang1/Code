using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TutorialToggle : MonoBehaviour
{
    public Toggle tutorialToggle;
    // Start is called before the first frame update
    void Start()
    {
        PlayerPrefs.GetString("Tutorial", "OFF");
    }

    // Update is called once per frame
    void Update()
    {
        if (tutorialToggle.isOn)
        {
            PlayerPrefs.SetString("Tutorial", "ON");
        }
        else
        {
            PlayerPrefs.SetString("Tutorial", "OFF");
        }
    }
}
