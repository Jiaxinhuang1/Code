using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Teleporter : MonoBehaviour
{
    public GameObject Alien;
    public GameObject Robot;
    public GameObject TeleportOne, TeleportTwo;
    public GameObject TeleportThree, TeleportFour;
    public AudioSource playerAudio;
    public AudioClip[] sounds;

    private void Start()
    {
        TeleportThree = GameObject.Find("TLoc3");
        Debug.Log(TeleportThree);
        TeleportFour = GameObject.Find("TLoc4");
        Debug.Log(TeleportFour);

    }
    private void OnTriggerEnter(Collider collision)
    {
        string nameInfo = collision.gameObject.name;
        Debug.Log(nameInfo);
        // if (collision.gameObject.CompareTag("Teleporter"))
        if(nameInfo.Contains("Teleporter") && nameInfo.Contains("1")){
            
            Alien.transform.position = TeleportOne.transform.position;
            Robot.transform.position = TeleportOne.transform.position;
            playerAudio.PlayOneShot(sounds[0], .5f);
        }
        // if (collision.gameObject.CompareTag("Teleporter2"))
        if(nameInfo.Contains("Teleporter") && nameInfo.Contains("2")){
            Alien.transform.position = TeleportTwo.transform.position;
            Robot.transform.position = TeleportTwo.transform.position;
            playerAudio.PlayOneShot(sounds[0], .5f);
        }

        if(nameInfo.Contains("Teleporter") && nameInfo.Contains("3")){
            Alien.transform.position = TeleportFour.transform.position;
            Robot.transform.position = TeleportFour.transform.position;
            playerAudio.PlayOneShot(sounds[0], .5f);
        }
        // if (collision.gameObject.CompareTag("Teleporter2"))
        if(nameInfo.Contains("Teleporter") && nameInfo.Contains("4")){
            Alien.transform.position = TeleportThree.transform.position;
            Robot.transform.position = TeleportThree.transform.position;
            playerAudio.PlayOneShot(sounds[0], .5f);
        }
            

        
    }
}
