using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class LeaderBoadManager : MonoBehaviour
{
    // initiate current player input and name
    private string playerName;
    public InputField playerNameInput;

    // initiate text for end leaderboard information
    public Text rankOneName;
    public Text rankTwoName;
    public Text rankThreeName;
    public Text rankFourName;
    public Text rankFiveName;
    public Text rankOneScore;
    public Text rankTwoScore;
    public Text rankThreeScore;
    public Text rankFourScore;
    public Text rankFiveScore;
    private int rank1Score;
    private int rank2Score;
    private int rank3Score;
    private int rank4Score;
    private int rank5Score;

    // initiate current player info
    public Text namePlayer;
    public Text scorePlayer;
    public GameObject gameOverPanel;

    // initiate other script to call public variables across scripts
    public PlayerDetection playerDetection;
    public PlayerMovement playerMovement;

    // initiate highlight for current leaderboard rank position
    public GameObject highLight;
    private RectTransform highLightRT;

    public bool isChanged;

    // Start is called before the first frame update
    void Start()
    {
        // get the rectTransform of highlight gameobject
        highLightRT = highLight.GetComponent<RectTransform>();

        isChanged = false;

        // get the ranking names from player prefs and assign it to respective text
        // if empty, set default to Player
        rankOneName.text = PlayerPrefs.GetString("rankOneName", "Player");
        rankTwoName.text = PlayerPrefs.GetString("rankTwoName", "Player");
        rankThreeName.text = PlayerPrefs.GetString("rankThreeName", "Player");
        rankFourName.text = PlayerPrefs.GetString("rankFourName", "Player");
        rankFiveName.text = PlayerPrefs.GetString("rankFiveName", "Player");

        // get the ranking score from player prefs
        // if empty, set default to 0
        rank1Score = PlayerPrefs.GetInt("rankOneScore", 0);
        rank2Score = PlayerPrefs.GetInt("rankTwoScore", 0);
        rank3Score = PlayerPrefs.GetInt("rankThreeScore", 0);
        rank4Score = PlayerPrefs.GetInt("rankFourScore", 0);
        rank5Score = PlayerPrefs.GetInt("rankFiveScore", 0);

        // convert player prefs ranking score to string and assign it
        rankOneScore.text = rank1Score.ToString("00");
        rankTwoScore.text = rank2Score.ToString("00");
        rankThreeScore.text = rank3Score.ToString("00");
        rankFourScore.text = rank4Score.ToString("00");
        rankFiveScore.text = rank5Score.ToString("00");



    }

    // Update is called once per frame
    void Update()
    {
        // get the score variable from player detection script
        scorePlayer.text = playerDetection.score.ToString("00");
        // reset the player prefs if press Delete
        if (Input.GetKeyDown(KeyCode.Delete))
        {
            ResetAllPrefs();
        }
    }

    public void ConfirmName()
    {
        // start the gameplay but setting the start bool in player movement script to true
        playerMovement.start = true;

        // set current player name to Player if player does not write anything in input field
        if (playerNameInput.text == "")
        {
            playerName = "Player";
            namePlayer.text = "Player";
        }
        // else set the current player name to what is written in the input field
        else
        {
            playerName = playerNameInput.text;
            namePlayer.text = playerNameInput.text;
        }
    }

    public void LoseGame()
    {
        if (!isChanged)
        {
            // get the score variable from player detection script
            scorePlayer.text = playerDetection.score.ToString("00");

            // if the score is greater than or equal to the score in rank one, 
            // set current name/score as rank one and move the rest of the rankings down
            if (playerDetection.score >= rank1Score)
            {
                PlayerPrefs.SetString("rankFiveName", rankFourName.text);
                PlayerPrefs.SetInt("rankFiveScore", rank4Score);
                PlayerPrefs.SetString("rankFourName", rankThreeName.text);
                PlayerPrefs.SetInt("rankFourScore", rank3Score);
                PlayerPrefs.SetString("rankThreeName", rankTwoName.text);
                PlayerPrefs.SetInt("rankThreeScore", rank2Score);
                PlayerPrefs.SetString("rankTwoName", rankOneName.text);
                PlayerPrefs.SetInt("rankTwoScore", rank1Score);

                PlayerPrefs.SetString("rankOneName", playerName);
                PlayerPrefs.SetInt("rankOneScore", playerDetection.score);

                //highLightRT.SetInsetAndSizeFromParentEdge(RectTransform.Edge.Top, 85, highLightRT.rect.height);
                // move the position of the highlight to place below the ranking position
                highLightRT.anchoredPosition = new Vector3(-1, 74, 0);

            }
            // if the score is greater than or equal to the score in rank two,
            // set current name/score as rank two and move the rest of the rankings down
            else if (playerDetection.score >= rank2Score)
            {
                PlayerPrefs.SetString("rankFiveName", rankFourName.text);
                PlayerPrefs.SetInt("rankFiveScore", rank4Score);
                PlayerPrefs.SetString("rankFourName", rankThreeName.text);
                PlayerPrefs.SetInt("rankFourScore", rank3Score);
                PlayerPrefs.SetString("rankThreeName", rankTwoName.text);
                PlayerPrefs.SetInt("rankThreeScore", rank2Score);

                PlayerPrefs.SetString("rankTwoName", playerName);
                PlayerPrefs.SetInt("rankTwoScore", playerDetection.score);

                //highLightRT.SetInsetAndSizeFromParentEdge(RectTransform.Edge.Top, 115, highLightRT.rect.height);
                highLightRT.anchoredPosition = new Vector3(-1, 43, 0);
            }
            // if the score is greater than or equal to the score in rank three
            // set current name/score as rank three and move the rest of the rankings down
            else if (playerDetection.score >= rank3Score)
            {
                PlayerPrefs.SetString("rankFiveName", rankFourName.text);
                PlayerPrefs.SetInt("rankFiveScore", rank4Score);
                PlayerPrefs.SetString("rankFourName", rankThreeName.text);
                PlayerPrefs.SetInt("rankFourScore", rank3Score);

                PlayerPrefs.SetString("rankThreeName", playerName);
                PlayerPrefs.SetInt("rankThreeScore", playerDetection.score);

                //highLightRT.SetInsetAndSizeFromParentEdge(RectTransform.Edge.Top, 145, highLightRT.rect.height);
                highLightRT.anchoredPosition = new Vector3(-1, 13, 0);
            }
            // if the score is greater than or equal to the score in rank four
            // set current name/score as rank four and move the rest of the rankings down
            else if (playerDetection.score >= rank4Score)
            {
                PlayerPrefs.SetString("rankFiveName", rankFourName.text);
                PlayerPrefs.SetInt("rankFiveScore", rank4Score);

                PlayerPrefs.SetString("rankFourName", playerName);
                PlayerPrefs.SetInt("rankFourScore", playerDetection.score);

                //highLightRT.SetInsetAndSizeFromParentEdge(RectTransform.Edge.Top, 175, highLightRT.rect.height);
                highLightRT.anchoredPosition = new Vector3(-1, -17, 0);
            }
            // if the score is greater than or equal to the score in rank five 
            // set current name/score as rank five
            else if (playerDetection.score >= rank5Score)
            {
                PlayerPrefs.SetString("rankFiveName", playerName);
                PlayerPrefs.SetInt("rankFiveScore", playerDetection.score);

                //highLightRT.SetInsetAndSizeFromParentEdge(RectTransform.Edge.Top, 205, highLightRT.rect.height);
                highLightRT.anchoredPosition = new Vector3(-1, -47, 0);
            }

            // change the text in leaderboard from the player prefs that was changed above
            rankOneName.text = PlayerPrefs.GetString("rankOneName", "Player");
            rankTwoName.text = PlayerPrefs.GetString("rankTwoName", "Player");
            rankThreeName.text = PlayerPrefs.GetString("rankThreeName", "Player");
            rankFourName.text = PlayerPrefs.GetString("rankFourName", "Player");
            rankFiveName.text = PlayerPrefs.GetString("rankFiveName", "Player");

            rank1Score = PlayerPrefs.GetInt("rankOneScore", 0);
            rank2Score = PlayerPrefs.GetInt("rankTwoScore", 0);
            rank3Score = PlayerPrefs.GetInt("rankThreeScore", 0);
            rank4Score = PlayerPrefs.GetInt("rankFourScore", 0);
            rank5Score = PlayerPrefs.GetInt("rankFiveScore", 0);

            rankOneScore.text = rank1Score.ToString("00");
            rankTwoScore.text = rank2Score.ToString("00");
            rankThreeScore.text = rank3Score.ToString("00");
            rankFourScore.text = rank4Score.ToString("00");
            rankFiveScore.text = rank5Score.ToString("00");

            isChanged = true;
        }
    }

    public void ResetAllPrefs()
    {
        PlayerPrefs.SetString("rankFiveName", "Player");
        PlayerPrefs.SetInt("rankFiveScore", 0);
        PlayerPrefs.SetString("rankFourName", "Player");
        PlayerPrefs.SetInt("rankFourScore", 0);
        PlayerPrefs.SetString("rankThreeName", "Player");
        PlayerPrefs.SetInt("rankThreeScore", 0);
        PlayerPrefs.SetString("rankTwoName", "Player");
        PlayerPrefs.SetInt("rankTwoScore", 0);
        PlayerPrefs.SetString("rankOneName", "Player");
        PlayerPrefs.SetInt("rankOneScore", 0);

        rankOneName.text = PlayerPrefs.GetString("rankOneName", "Player");
        rankTwoName.text = PlayerPrefs.GetString("rankTwoName", "Player");
        rankThreeName.text = PlayerPrefs.GetString("rankThreeName", "Player");
        rankFourName.text = PlayerPrefs.GetString("rankFourName", "Player");
        rankFiveName.text = PlayerPrefs.GetString("rankFiveName", "Player");

        rank1Score = PlayerPrefs.GetInt("rankOneScore", 0);
        rank2Score = PlayerPrefs.GetInt("rankTwoScore", 0);
        rank3Score = PlayerPrefs.GetInt("rankThreeScore", 0);
        rank4Score = PlayerPrefs.GetInt("rankFourScore", 0);
        rank5Score = PlayerPrefs.GetInt("rankFiveScore", 0);

        rankOneScore.text = rank1Score.ToString("00");
        rankTwoScore.text = rank2Score.ToString("00");
        rankThreeScore.text = rank3Score.ToString("00");
        rankFourScore.text = rank4Score.ToString("00");
        rankFiveScore.text = rank5Score.ToString("00");
    }
}
