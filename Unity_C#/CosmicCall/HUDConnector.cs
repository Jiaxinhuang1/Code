using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using Hashtable = ExitGames.Client.Photon.Hashtable;
using Photon.Pun;
using Photon.Realtime;

public class HUDConnector : MonoBehaviourPunCallbacks
{
    public Slider healthBar;
    public Text healthText;
    public Text alienKillsText;
    public Text robotKillsText;
    public GameObject gunWeapon;
    public GameObject knifeWeapon;
    public GameObject gunImage;
    public GameObject knifeImage;

    private BetterPlayerController betterPlayerController;

    public override void OnEnable() {
        base.OnEnable();
    }
    
    public override void OnDisable() {
        base.OnDisable();
    }
    

    private void Start()
    {
        // get the BetterPlayerController script from the parent gameobject
        betterPlayerController = gameObject.GetComponentInParent<BetterPlayerController>();
    }
    private void Update()
    {
        // Set the value of the text and slider to the health variable of the BetterPlayerController script
        healthText.text = betterPlayerController.health.ToString();
        healthBar.value = betterPlayerController.health;
        // set the weapon HUD to match the weapon the player has equipped
        if (gunWeapon.activeInHierarchy)
        {
            gunImage.SetActive(true);
        }
        else
        {
            gunImage.SetActive(false);
        }
        if (knifeWeapon.activeInHierarchy)
        {
            knifeImage.SetActive(true);
        }
        else
        {
            knifeImage.SetActive(false);
        }
    }

    public override void OnRoomPropertiesUpdate(Hashtable propertiesThatChanged){
        Debug.Log("here");
        int alienScore, robotScore  = 0;
        Hashtable robotHash, alienHash;
        robotHash = new Hashtable();
        try{
            robotScore = (int)PhotonNetwork.CurrentRoom.CustomProperties["robotScore"];
        } catch(Exception e){
            Debug.Log(e);
            robotScore = 0;
            robotHash.Add("robotScore", robotScore);
            PhotonNetwork.CurrentRoom.SetCustomProperties(robotHash);
            return;
        }
        robotKillsText.text = robotScore.ToString("00");
        alienHash = new Hashtable();
        try{
            alienScore = (int)PhotonNetwork.CurrentRoom.CustomProperties["alienScore"];
        } catch(Exception e){
            Debug.Log(e);
            alienScore = 0;
            robotHash.Add("alienScore", alienScore);
            PhotonNetwork.CurrentRoom.SetCustomProperties(alienHash);
            return;
        }
        alienKillsText.text = alienScore.ToString("00");
        Debug.Log("separator");
        int myScore = 0;
        Hashtable myScoreHash;
        myScoreHash = new Hashtable();
        try
        {
            myScore = (int)PhotonNetwork.LocalPlayer.CustomProperties["score"];
        }
        catch(Exception e)
        {
            Debug.Log(e);
            myScore = 0;
            myScoreHash.Add("score", myScore);
            PhotonNetwork.LocalPlayer.SetCustomProperties(myScoreHash);
            return;
        }
    }
}
