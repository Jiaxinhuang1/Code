using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerCustom : MonoBehaviour
{
    // This script is attached to empty player object in gameplay to display the character look in gameplay scene

    // integers that will store the index of each part
    private int hair;
    private int eye;
    private int clothes;
    private int weapons;
    private int hairColor;
    private int eyeColor;
    private int clothesColor;

    private GameObject slotSave;
    private CharCusSave charCusSave;
    public Text playerName;
    public GameObject hairStyle;
    public GameObject eyeStyle;
    public GameObject clothesStyle;

    // create multiple lists for each object and body part 
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
        slotSave = GameObject.FindGameObjectWithTag("SlotSave");
        charCusSave = slotSave.GetComponent<CharCusSave>();

        // check to see which slot player is on and get the index of the saved slot data to each body part
        // set the name of the player on status based on player prefs
        if (charCusSave.isSlotOne)
        {
            hair = PlayerPrefs.GetInt("OneHair", 10);
            eye = PlayerPrefs.GetInt("OneEye", 10);
            clothes = PlayerPrefs.GetInt("OneClothes", 10);
            weapons = PlayerPrefs.GetInt("OneWeapon", 0);
            playerName.text = PlayerPrefs.GetString("OneName", "PlayerName");
            hairColor = PlayerPrefs.GetInt("OneHairColor", 0);
            eyeColor = PlayerPrefs.GetInt("OneEyeColor", 0);
            clothesColor = PlayerPrefs.GetInt("OneClothesColor", 0);
        }
        else if (charCusSave.isSlotTwo)
        {
            hair = PlayerPrefs.GetInt("TwoHair", 10);
            eye = PlayerPrefs.GetInt("TwoEye", 10);
            clothes = PlayerPrefs.GetInt("TwoClothes", 10);
            weapons = PlayerPrefs.GetInt("TwoWeapon", 0);
            playerName.text = PlayerPrefs.GetString("TwoName", "PlayerName");
            hairColor = PlayerPrefs.GetInt("TwoHairColor", 0);
            eyeColor = PlayerPrefs.GetInt("TwoEyeColor", 0);
            clothesColor = PlayerPrefs.GetInt("TwoClothesColor", 0);
        }
        else if (charCusSave.isSlotThree)
        {
            hair = PlayerPrefs.GetInt("ThreeHair", 10);
            eye = PlayerPrefs.GetInt("ThreeEye", 10);
            clothes = PlayerPrefs.GetInt("ThreeClothes", 10);
            weapons = PlayerPrefs.GetInt("ThreeWeapon", 0);
            playerName.text = PlayerPrefs.GetString("ThreeName", "PlayerName");
            hairColor = PlayerPrefs.GetInt("ThreeHairColor", 0);
            eyeColor = PlayerPrefs.GetInt("ThreeEyeColor", 0);
            clothesColor = PlayerPrefs.GetInt("ThreeClothesColor", 0);
        }
        Debug.Log(hair + eye + clothes);

        // using the index from player prefs, show only the active ones
        hairOptions[hair].SetActive(true);
        eyeOptions[eye].SetActive(true);
        clothesOptions[clothes].SetActive(true);
        weaponsOptions[weapons].SetActive(true);

        // loop through entire list and do not show it if it is not the current index
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

    // Update is called once per frame
    void Update()
    {
        
    }
}
