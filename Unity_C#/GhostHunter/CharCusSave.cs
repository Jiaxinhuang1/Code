using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class CharCusSave : MonoBehaviour
{
    //This script is attached to an empty gameobject that will be on both scenes to control which save slot player is currently on
    public bool isSlotOne;
    public bool isSlotTwo;
    public bool isSlotThree;

    private Toggle SlotOneToggle;
    private Toggle SlotTwoToggle;
    private Toggle SlotThreeToggle;

    private Animator canvasAnim;
    private MenuManager menuManager;
    private InputField nameInput;
  
    private static CharCusSave instance;
    private void Awake()
    {
        // Keep the object even when scene change but destroy it if there is a duplicate
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(instance);
        }
        else
        {
            Destroy(gameObject);
        }
    }
    // Start is called before the first frame update
    void Start()
    {
        isSlotOne = false;
        isSlotTwo = false;
        isSlotThree = false;
        
        // Get the toggles from the gameobjects with respective tags
        SlotOneToggle = GameObject.FindGameObjectWithTag("SlotOne").GetComponent<Toggle>();
        SlotTwoToggle = GameObject.FindGameObjectWithTag("SlotTwo").GetComponent<Toggle>();
        SlotThreeToggle = GameObject.FindGameObjectWithTag("SlotThree").GetComponent<Toggle>();

        canvasAnim = GameObject.FindGameObjectWithTag("Canvas").GetComponent<Animator>();
        menuManager = GameObject.FindGameObjectWithTag("MenuManager").GetComponent<MenuManager>();
        nameInput = GameObject.FindGameObjectWithTag("NameInput").GetComponent<InputField>();

    }

    // Update is called once per frame
    void Update()
    {
        
    }

    // function called when confirm button on save and load is clicked
    public void SlotChoosen()
    {
        // Set bool depending on which slot toggle is on
        // If the slot had loaded data, fade to gameplay scene
        // Else if the slot is empty, play the open customization animation
        if (SlotOneToggle.isOn)
        {
            isSlotOne = true;
            isSlotTwo = false;
            isSlotThree = false;
            if ((PlayerPrefs.GetString("SlotOne", "empty") == "load"))
            {
                menuManager.Fade();
            }
            else
            {
                canvasAnim.Play("OpenCustomization");
            }
        }
        else if (SlotTwoToggle.isOn)
        {
            isSlotTwo = true;
            isSlotOne = false;
            isSlotThree = false;
            if ((PlayerPrefs.GetString("SlotTwo", "empty") == "load"))
            {
                menuManager.Fade();
            }
            else
            {
                canvasAnim.Play("OpenCustomization");
            }
        }
        else if (SlotThreeToggle.isOn)
        {
            isSlotThree = true;
            isSlotOne = false;
            isSlotTwo = false;
            if ((PlayerPrefs.GetString("SlotThree", "empty") == "load"))
            {
                SceneManager.LoadScene("Gameplay");
            }
            else
            {
                canvasAnim.Play("OpenCustomization");
            }
        }
    }

    // function called when moving from gameplay to menu to destroy this gameobject
    public void DestroyThis()
    {
        Destroy(gameObject);
    }

    // function called when confirm button in customization is clicked to save the name input data in player prefs
    public void NameConfirm()
    {
        if (isSlotOne)
        {
            if (nameInput.text == "")
            {
                PlayerPrefs.SetString("OneName", "PlayerOne");
            }
            else 
            {
                PlayerPrefs.SetString("OneName", nameInput.text);
            }
        }
        else if (isSlotTwo)
        {
            if (nameInput.text == "")
            {
                PlayerPrefs.SetString("TwoName", "PlayerTwo");
            }
            else
            {
                PlayerPrefs.SetString("TwoName", nameInput.text);
            }
        }
        else if (isSlotThree)
        {
            if (nameInput.text == "")
            {
                PlayerPrefs.SetString("ThreeName", "PlayerTwo");
            }
            else
            {
                PlayerPrefs.SetString("ThreeName", nameInput.text);
            }
        }
    }
}
