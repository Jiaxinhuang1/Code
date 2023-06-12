using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DisplayName : MonoBehaviour
{
    // This script is attached to each player name in save and load which displays the name from the string from player prefs
    private Text playerName;
    public string slotNumber;
    // Start is called before the first frame update
    void Start()
    {
        // set the text based on playerprefs on each slot
        playerName = this.gameObject.GetComponent<Text>();
        playerName.text = PlayerPrefs.GetString(slotNumber + "Name");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
