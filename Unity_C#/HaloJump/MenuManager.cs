using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MenuManager : MonoBehaviour
{
    // initiate leaderboard information variable
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

    // Start is called before the first frame update
    void Start()
    {
        // get ranking name from player prefs and assign it
        rankOneName.text = PlayerPrefs.GetString("rankOneName", "Player");
        rankTwoName.text = PlayerPrefs.GetString("rankTwoName", "Player");
        rankThreeName.text = PlayerPrefs.GetString("rankThreeName", "Player");
        rankFourName.text = PlayerPrefs.GetString("rankFourName", "Player");
        rankFiveName.text = PlayerPrefs.GetString("rankFiveName", "Player");

        // get ranking score from player prefs
        rank1Score = PlayerPrefs.GetInt("rankOneScore", 0);
        rank2Score = PlayerPrefs.GetInt("rankTwoScore", 0);
        rank3Score = PlayerPrefs.GetInt("rankThreeScore", 0);
        rank4Score = PlayerPrefs.GetInt("rankFourScore", 0);
        rank5Score = PlayerPrefs.GetInt("rankFiveScore", 0);

        // convert the int to string and assign it
        rankOneScore.text = rank1Score.ToString("00");
        rankTwoScore.text = rank2Score.ToString("00");
        rankThreeScore.text = rank3Score.ToString("00");
        rankFourScore.text = rank4Score.ToString("00");
        rankFiveScore.text = rank5Score.ToString("00");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
