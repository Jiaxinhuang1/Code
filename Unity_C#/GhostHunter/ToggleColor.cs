using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ToggleColor : MonoBehaviour
{
    // This script is attached to each hair, eye, clothes color toggle which changed the image of a bodypart to the color
    // stated in the inspector
    private Toggle toggle;
    public Color color;
    public GameObject bodyPart;
    public int colorIndex;
    public CharCusSave charCusSave;
    public string body;
    // Start is called before the first frame update
    void Start()
    {
        toggle = this.GetComponent<Toggle>();
    }

    // Update is called once per frame
    void Update()
    {
        // when toggle is on get the image of the children of the gameobject and change its color
        if (toggle.isOn)
        {
            bodyPart.GetComponentInChildren<Image>().color = color;
            if (charCusSave.isSlotOne)
            {
                PlayerPrefs.SetInt("One" + body + "Color", colorIndex);
            }
            else if (charCusSave.isSlotTwo)
            {
                PlayerPrefs.SetInt("Two" + body + "Color", colorIndex);
            }
            else if (charCusSave.isSlotThree)
            {
                PlayerPrefs.SetInt("Three" + body + "Color", colorIndex);
            }
        }
    }
}
