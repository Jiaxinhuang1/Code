using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SaveLoadChar : MonoBehaviour
{
    // This script is attached to the Characters in the Save and Load Panel to display or not display the character
    // based on saved data of each bodypart in the player prefs.
    private int hair;
    private int eye;
    private int clothes;
    private int weapons;
    private int hairColor;
    private int eyeColor;
    private int clothesColor;

    public string slotNumber;
    public GameObject hairStyle;
    public GameObject eyeStyle;
    public GameObject clothesStyle;
    public GameObject placeHolder;

    private GameObject slotSave;
    private CharCusSave charCusSave;

    // Creates list of body parts to loop through 
    [Header("Hair Cycle List")]
    public List<GameObject> hairOptions = new List<GameObject>();

    [Header("Eye Cycle List")]
    public List<GameObject> eyeOptions = new List<GameObject>();

    [Header("Clothes Cycle List")]
    public List<GameObject> clothesOptions = new List<GameObject>();

    [Header("Weapons Cycle List")]
    public List<GameObject> weaponsOptions = new List<GameObject>();

    [Header("Color Cycle List")]
    public List<Color> colorOptions = new List<Color>();
    // Start is called before the first frame update
    void Start()
    {
        // Get the script from the slotSave gameobject that has the tag SlotSave
        slotSave = GameObject.FindGameObjectWithTag("SlotSave");
        charCusSave = slotSave.GetComponent<CharCusSave>();

        DisplayChar();
    }

    // Displays the character based on what is saved in the Player prefs of hair, eye, clothes, and weapons
    public void DisplayChar()
    {
        // Get the integer from the saved data (the index of the lists)
        hair = PlayerPrefs.GetInt(slotNumber + "Hair", 0);
        eye = PlayerPrefs.GetInt(slotNumber + "Eye", 0);
        clothes = PlayerPrefs.GetInt(slotNumber + "Clothes", 0);
        weapons = PlayerPrefs.GetInt(slotNumber + "Weapon", 0);
        hairColor = PlayerPrefs.GetInt(slotNumber + "HairColor", 0);
        eyeColor = PlayerPrefs.GetInt(slotNumber + "EyeColor", 0);
        clothesColor = PlayerPrefs.GetInt(slotNumber + "ClothesColor", 0);
        Debug.Log((slotNumber, hairColor, eyeColor, clothesColor).ToString());

        // if there is no saved data, then the character does not show up in the save and load panel at that slot
        if ((PlayerPrefs.GetString("Slot" + slotNumber, "empty") != "load"))
        {
            this.gameObject.SetActive(false);
            placeHolder.SetActive(true);
        }
        // if there is data, display character
        else
        {
            placeHolder.SetActive(false);
            this.gameObject.SetActive(true);

            // used the index from playerprefs of each body part and display it
            hairOptions[hair].SetActive(true);
            eyeOptions[eye].SetActive(true);
            clothesOptions[clothes].SetActive(true);
            weaponsOptions[weapons].SetActive(true);

            // loop through the rest of the body parts list and do not display it if it is not the saved index
            for (int i = 0; i < hairOptions.Count; i++)
            {
                if (i != hair)
                {
                    hairOptions[i].SetActive(false);
                }
            }
            for (int i = 0; i < eyeOptions.Count; i++)
            {
                if (i != eye)
                {
                    eyeOptions[i].SetActive(false);
                }
            }
            for (int i = 0; i < clothesOptions.Count; i++)
            {
                if (i != clothes)
                {
                    clothesOptions[i].SetActive(false);
                }
            }
            for (int i = 0; i < weaponsOptions.Count; i++)
            {
                if (i != weapons)
                {
                    weaponsOptions[i].SetActive(false);
                }
            }

            // change the color of the body parts depending on saved data
            hairStyle.GetComponentInChildren<Image>().color = colorOptions[hairColor];
            eyeStyle.GetComponentInChildren<Image>().color = colorOptions[eyeColor];
            clothesStyle.GetComponentInChildren<Image>().color = colorOptions[clothesColor];
        }

    }
}
