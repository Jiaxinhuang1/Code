using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class Timer : MonoBehaviour
{
    // Start is called before the first frame update
    public int secondsLeft = 59;
    public int minutesLeft = 10;
    public bool takingAway = false;

    public bool isTimesUp = false;
    private bool isTiming = false;
    //public AudioSource timeUpSound;

    public int activeTime = 3;

    public bool isIndicated = false;


    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        // keep counting down if there is still time left
        if (takingAway == false )
        {
            StartCoroutine(TimerCount());
        }

    }

    IEnumerator TimerCount()
    {
        takingAway = true;
        // take away time every second
        yield return new WaitForSeconds(1);
        secondsLeft -= 1;
        activeTime -= 1;    //countdown for team indicator panel
        if (activeTime == 0)
        {
            isIndicated = true;
            //indicatorPanel.SetActive(false);
            activeTime = -1;
        }
        // sec back to 59 and minutes minus one for every minute passed
        if (secondsLeft <= 0 && minutesLeft != 0)
        {
            secondsLeft = 59;
            minutesLeft -= 1;
        }
        /* start playing the times up sound when there is only 10 secodns left
        else if (minutesLeft == 0 && secondsLeft < 10 && isTiming == false)
        {
            timeUpSound.Play();
            isTiming = true;
        }*/
        // when the time is up 00:00 set the times up panel to show game results
        if (secondsLeft == 0 && minutesLeft == 0)
        {
            isTimesUp = true;
            //Time.timeScale = 0;
            //timeUpPanel.SetActive(true);

        }
        // when second is one digit make sure there is a 0 in front of the digit
        // if (secondsLeft < 10)
        // {
        //     timeText.GetComponent<Text>().text = "0" + minutesLeft + ":0" + secondsLeft;
        // }
        // else
        // {
        //     timeText.GetComponent<Text>().text = "0" + minutesLeft + ":" + secondsLeft;
        // }
        // timeText.GetComponent<Text>().text = minutesLeft.ToString("00") + ":" + secondsLeft.ToString("00");
        takingAway = false;
    }
}
