using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using Hashtable = ExitGames.Client.Photon.Hashtable;
using Photon.Pun;
using Photon.Realtime;

public class TimePlayer : MonoBehaviourPunCallbacks
{
    // Start is called before the first frame update
    public GameObject timeText;

    public GameObject timeUpPanel;
    public bool didCalculations;

    public GameObject indicatorPanel;

    private GameObject timerGameobject;
    private Timer timer;

    public GameObject playerNameField;
    public GameObject playerKillsField;
    public RectTransform playerKillsScrollView;
    public RectTransform killsScroll;
    public GameObject player;



    void Start()
    {
        // Get the timer script from the gameobject with timer tag
        timerGameobject = GameObject.FindGameObjectWithTag("Timer");
        timer = timerGameobject.GetComponent<Timer>();

        // display the time in the timeText
        timeText.GetComponent<Text>().text = timer.minutesLeft.ToString("00") + ":" + timer.secondsLeft.ToString("00");

        timeUpPanel.SetActive(false);
        indicatorPanel.SetActive(true);
        didCalculations = false;
    }

    // Update is called once per frame
    void Update()
    {
        // timeText.GetComponent<Text>().text = timer.minutesLeft.ToString("00") + ":" + timer.secondsLeft.ToString("00");
        // show result when time is up
        if (timer.isTimesUp)
        {
            Cursor.lockState = CursorLockMode.None;
            if(!didCalculations){ // want to unlock the mouse automatically now that the game is over
                player.GetComponent<BetterPlayerController>().isPausable = false;
                player.GetComponent<BetterPlayerController>().paused = true;
                WinnerAndStats();
                timer.isIndicated = false;
                timeUpPanel.SetActive(true);
            }
            
            // timer.isTimesUp = false;
        }
        // show team indicator for 3 sec and disappear
        if (timer.isIndicated)
        {
            indicatorPanel.SetActive(false);
        }
        if(!timer.isTimesUp){
            timeText.GetComponent<Text>().text = timer.minutesLeft.ToString("00") + ":" + timer.secondsLeft.ToString("00");
        }
        
    }

    void WinnerAndStats(){
        //Color robotColor = new Color(0.9529412f, 0.6156863f, 0.1372549f);
        timeText.GetComponent<Text>().text = "00:00"; // need to get that final second
        Color robotColor = new Color32(255, 100, 0, 255);
        Color alienColor = new Color32(255, 255, 255, 255);
        //TODO: Figure out which team won
        int robotScore, alienScore = 0;
        int winningTeam, myTeam = -1;
        try{
            robotScore = (int) PhotonNetwork.CurrentRoom.CustomProperties["robotScore"];
        } catch(Exception e){
            //We really shouldn't hit this
            robotScore = 0;
        }
        try{
            alienScore = (int) PhotonNetwork.CurrentRoom.CustomProperties["alienScore"];
        } catch(Exception e){
            //We really shouldn't hit this
            alienScore = 0;
        }
        
        if(robotScore > alienScore){
            winningTeam = 0;
        } else if(alienScore > robotScore){
            winningTeam = 1;
        } else{
            winningTeam = 2; //signifies a tie --> just in case 
        }
        string myTag = this.gameObject.tag;
        string myTeamName = "";
        if(myTag.Contains("Robot")){
            myTeam = 0;
            myTeamName = "Robot";
        }
        if(myTag.Contains("Alien")){
            myTeam = 1;
            myTeamName = "Alien";
        }
        timer.isIndicated = false;
        timer.activeTime = 3;
        if(myTeam == winningTeam){
            //TODO: Turn on you win Text
            Debug.Log("You win");
            indicatorPanel.GetComponentInChildren<Text>().text = myTeamName.ToUpper() + " VICTORY!";
            indicatorPanel.SetActive(true);
            timer.activeTime = 3;
        } 
        if(myTeam != winningTeam && winningTeam != 2){
            //TODO: You lost text
            Debug.Log("You lost");
            indicatorPanel.GetComponentInChildren<Text>().text = myTeamName.ToUpper() + " IS DEFEATED!";
            indicatorPanel.SetActive(true);
            timer.activeTime = 3;
        }
        if(winningTeam == 2){
            //TODO: You tied
            Debug.Log("You tied");
            indicatorPanel.GetComponentInChildren<Text>().text = "It is a TIE!";
            indicatorPanel.SetActive(true);
            timer.activeTime = 3;
        }


        //TODO: Figure out who has how many kills
        Player[] players = PhotonNetwork.PlayerList;
        Player[] sortedPlayers = new Player[players.Length];
        int[] scores = new int[players.Length];
        int currScore = 0;
        //So first I want to get all my scores
        for(int i = 0; i < players.Length; i++){
            try{
                currScore = (int) players[i].CustomProperties["score"];
            } catch(Exception e){
                currScore = 0;
            }
            scores[i] = currScore;
        }
        //SOrt my scores (most efficient way that doesn't require my own sorting algo)
        Array.Sort(scores);
        //Put it in greatest to least order
        Array.Reverse(scores);
        int index = scores.Length;
        bool addedToSorted = false;
        int newScore = 0;
        for(int i = 0; i < scores.Length; i++){
            addedToSorted = false;
            for(int j = 0; j < players.Length; j++){
                try{
                        newScore = (int)players[j].CustomProperties["score"];
                    } catch (Exception e){
                        newScore = 0;
                        //This means that this player has not scored any points, which means there score is 0
                        sortedPlayers[i] = players[j];
                    }
                if(scores[i] == 0){
                    
                    
                    //just in case scores[i] == 0, but the player has more kills
                    continue;
                }
                if(scores[i] == newScore){
                    //I get the player with this score, and i put it in the correct position
                    sortedPlayers[i] = players[j];
                    addedToSorted = true;
                }
                
            }
            // if(!addedToSorted){
            //     sortedPlayers[i] == players[];
            // }
        }
        //I was too lazy to rename stuff properly so I set players = sortedPlayers, so players should be sorted now
        players = sortedPlayers;
        for (int i = 0; i < players.Length; i++)
        // foreach (Player p in PhotonNetwork.PlayerList)
        {
            Debug.Log("Curr player is: " + players[i].NickName + " and i is: " + i);
            GameObject playerNameText = Instantiate(playerNameField, playerKillsScrollView);
            GameObject playerKillText = Instantiate(playerKillsField, killsScroll);
            Debug.Log("Curr player team is: " + (int)players[i].CustomProperties["team"]);
            if( (int)players[i].CustomProperties["team"] == 0){
                Debug.Log("I am an Robot");
                playerNameText.GetComponent<Image>().color = robotColor;
            }
            else
            {
                Debug.Log("I am an Alien");
                playerNameText.GetComponent<Image>().color = alienColor;
            }

            if (players[i].CustomProperties["score"] == null)
            {
                Debug.Log("No Score");
                playerNameText.GetComponentInChildren<Text>().text = players[i].NickName;
                playerKillText.GetComponentInChildren<Text>().text = "0";
            }
            else
            {
                playerNameText.GetComponentInChildren<Text>().text = players[i].NickName;
                playerKillText.GetComponentInChildren<Text>().text = players[i].CustomProperties["score"].ToString();
                
            }
            //GameObject currPlayerObj = Instantiate(playerNameField, playerKillsScrollView);
            //currPlayerObj.GetComponentInChildren<Text>().text = players[i].NickName + "  " + players[i].CustomProperties["score"].ToString();
        }
        //Oh god this our 3rd loop for the same thing why did i do this complexity freaking sucks
        //Don't repeat this again;
        didCalculations = true;
    }
}
