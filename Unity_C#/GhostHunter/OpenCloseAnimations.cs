using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OpenCloseAnimations : MonoBehaviour
{
    // This script is attached an MenuManager empty gameobject which controls the keyboard shortcuts to open gameplay popups
    // rather than pressing on button with mouse
    private bool questOpened;
    private bool pauseOpened;
    private bool inventoryOpened;
    private bool mapOpened;
    public Animator anim;
    public AudioSource clickSound;
    // Start is called before the first frame update
    void Start()
    {
        questOpened = false;
        pauseOpened = false;
        inventoryOpened = false;
        mapOpened = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.P))
        {
            pauseAnim();
            clickSound.Play();
        }
        if (Input.GetKeyDown(KeyCode.M))
        {
            mapAnim();
            clickSound.Play();
        }
        if (Input.GetKeyDown(KeyCode.I))
        {
            inventoryAnim();
            clickSound.Play();
        }
        if (Input.GetKeyDown(KeyCode.H))
        {
            questAnim();
            clickSound.Play();
        }
    }

    // function called when h is pressed
    // if quest is already opened, then play close quest animation otherwise play open quest animation
    public void questAnim()
    {
        if (questOpened)
        {
            anim.Play("CloseQuest");
            questOpened = false;
            Debug.Log("Close Quest");
        }
        else
        {
            anim.Play("OpenQuest");
            Debug.Log("Open Quest");
            questOpened = true;
        }
    }

    // function called when m is pressed
    // if map is already opened, then play close map animation otherwise play open map animation
    public void mapAnim()
    {
        if (mapOpened)
        {
            anim.Play("CloseMap");
            mapOpened = false;
            //Debug.Log("Close Quest");
        }
        else
        {
            anim.Play("OpenMap");
            //Debug.Log("Open Quest");
            mapOpened = true;
        }
    }

    //function called when p is pressed 
    // if paused panel is already opened, then play close pause panel animation otherwise play open pause animation
    public void pauseAnim()
    {
        if (pauseOpened)
        {
            anim.Play("ClosePause");
            pauseOpened = false;
            //Debug.Log("Close Pause");
        }
        else
        {
            anim.Play("OpenPause");
            //Debug.Log("Open Pause");
            pauseOpened = true;
        }
    }

    // function called when i is pressed
    // if inventory is already opened, then play close inventory animation otherwise play open inventory animation
    public void inventoryAnim()
    {
        if (inventoryOpened)
        {
            anim.Play("CloseInventory");
            inventoryOpened = false;
            //Debug.Log("Close Pause");
        }
        else
        {
            anim.Play("OpenInventory");
            //Debug.Log("Open Pause");
            inventoryOpened = true;
        }
    }

    public void falseInven()
    {
        inventoryOpened = !inventoryOpened;
    }
}
