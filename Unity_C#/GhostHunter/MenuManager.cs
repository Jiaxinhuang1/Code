using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class MenuManager : MonoBehaviour
{
    // This script is attached to an empty MenuManager gameobject which controls the transition between scenes
    public Image blackScreen;
    public Animator blackAnim;
    public string sceneName;
    public AudioSource bgMusic;
    public Animator musicAnim;
    private GameObject slotSave;

    void Start()
    {
        slotSave = GameObject.FindGameObjectWithTag("SlotSave");
    }

    // Update is called once per frame
    void Update()
    {

    }

    // function called when change from menu to gameplay scene or vice versa
    public void Fade()
    {
        StartCoroutine(Fading());
    }

    // fades out and in (black image and sound) to scene 
    IEnumerator Fading()
    {
        blackAnim.SetBool("Fade", true);
        musicAnim.SetBool("Fade", true);
        //musicAnim.SetTrigger("FadeOut");
        // load the scene after it is completely fade to black
        yield return new WaitUntil(() => blackScreen.color.a == 1);
        SceneManager.LoadScene(sceneName);
    }

    // function called when exit button is clicked
    public void ExitGame()
    {
        Application.Quit();
    }

    //function called to destroy the slot save so it does not duplicate
    public void DestroyThis()
    {
        Destroy(slotSave);
    }

    // function called when pressed each slotnumber button in the options data panel
    public void ResetSlot(string slotNumber)
    {
        // resets the saved slots 
        PlayerPrefs.SetString("Slot" + slotNumber, "empty");
    }
}
