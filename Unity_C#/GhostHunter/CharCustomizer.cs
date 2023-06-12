using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CharCustomizer : MonoBehaviour
{
    // This Script is attached to HairStyleSlot, EyeStyleSlot, and ClothesStyleSlot which controls the character customization images

    // Creates list of body parts
    [Header("Body Part to Change")]
    public string bodyPart;
    
    [Header("Body Part Cycle List")]
    public List<GameObject> options = new List<GameObject>();

    public CharCusSave charCusSave;

    private int currentOption = 0;

    // function called with next arrow child button of the gameobject this script is attached to is clicked
    // Loops through the index and set current active
    public void NextOption()
    {
        currentOption++;
        if (currentOption >= options.Count)
        {
            // resets if cycle through entire list
            currentOption = 0;
        }
        options[currentOption].SetActive(true);
        for(int i = 0; i < options.Count; i++)
        {
            if (i != currentOption)
            {
                options[i].SetActive(false);
            }
        }
    }
    // function called with previous arrow child button of the gameobject this script is attached to is clicked
    // Loops through the index and set current active
    public void PreviousOption()
    {
        currentOption--;
        if (currentOption <= 0)
        {
            currentOption = options.Count - 1;
        }
        options[currentOption].SetActive(true);
        for (int i = 0; i < options.Count; i++)
        {
            if (i != currentOption)
            {
                options[i].SetActive(false);
            }
        }
    }

    // function called when confirma button from charactercustomization is clicked to save each body part index to player prefs
    // and set the slots to be load instead of empty
    public void ConfirmChoice()
    {
        if (charCusSave.isSlotOne)
        {
            PlayerPrefs.SetInt("One" + bodyPart, currentOption);
            PlayerPrefs.SetString("SlotOne", "load");
        }
        else if (charCusSave.isSlotTwo)
        {
            PlayerPrefs.SetInt("Two" + bodyPart, currentOption);
            PlayerPrefs.SetString("SlotTwo", "load");
        }
        else if (charCusSave.isSlotThree)
        {
            PlayerPrefs.SetInt("Three" + bodyPart, currentOption);
            PlayerPrefs.SetString("SlotThree", "load");
        }
    }
}
