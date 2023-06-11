using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CharacterSelect : MonoBehaviour
{
    public Animator playerAnim;
    public Toggle defaultChar;
    public Toggle angelChar;
    public Toggle devilChar;
    public GameObject lockedAngel;
    public GameObject lockedDevil;
    [SerializeField] private int highestScoreCount;
    public int damage;
    public int haloIncrement;

    // Start is called before the first frame update
    void Start()
    {
        highestScoreCount = PlayerPrefs.GetInt("rankOneScore", 0);
        if (highestScoreCount >= 40)
        {
            devilChar.interactable = true;
            angelChar.interactable = true;
        }
        else if (highestScoreCount >= 20)
        {
            angelChar.interactable = true;
            devilChar.interactable = false;
        }
        else
        {
            devilChar.interactable = false;
            angelChar.interactable = false;
        }
        if (!angelChar.interactable)
        {
            lockedAngel.SetActive(true);
        }
        else
        {
            lockedAngel.SetActive(false);
        }
        if (!devilChar.interactable)
        {
            lockedDevil.SetActive(true);
        }
        else
        {
            lockedDevil.SetActive(false);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void ConfirmChar()
    {
        if (defaultChar.isOn)
        {
            damage = 33;
            haloIncrement = 1;
            playerAnim.runtimeAnimatorController = Resources.Load("Original_Animator") as RuntimeAnimatorController;
        }
        else if (angelChar.isOn)
        {
            damage = 33;
            haloIncrement = 2;
            playerAnim.runtimeAnimatorController = Resources.Load("Angel_Animator") as RuntimeAnimatorController;
        }
        else if (devilChar.isOn)
        {
            damage = 15;
            haloIncrement = 1;
            playerAnim.runtimeAnimatorController = Resources.Load("Devil_Animator") as RuntimeAnimatorController;
        }
    }
}
