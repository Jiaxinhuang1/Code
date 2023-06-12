using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerDetection : MonoBehaviour
{
    // This script is attached to empty Player object which controls the state of the player in gameplay scene
    public Slider healthBar;
    public Slider manaBar;
    public AudioSource gruntSound;
    public AudioSource swordSound;
    public AudioSource loseSound;
    private int health;
    private int mana;
    public Animator anim;
    private bool done;
    // Start is called before the first frame update
    void Start()
    {
        // start with full health and mana
        health = 100;
        mana = 100;
        done = false;
    }

    // Update is called once per frame
    void Update()
    {
        // set the health bar value to health and play lose animation if player dies
        healthBar.value = health;
        manaBar.value = mana;
        if (health <= 0)
        {
            anim.Play("OpenLose");
            if (!done)
            {
                loseSound.Play();
                done = true;
            }
        }

        // for testing, press 1 to decrease health and 2 to decrease mana
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            if (health > 0)
            {
                health -= 10;
                gruntSound.Play();
            }
        }
        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            if (mana > 0)
            { 
            mana -= 10;
            swordSound.Play();
            }

        }
    }

    // function called when respawn button is pressed to reset player state
    public void respawnCharacter()
    {
        health = 100;
        mana = 100;
        done = false;
    }
}
