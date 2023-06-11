using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System;
using Random = UnityEngine.Random;

public class UIManager : MonoBehaviour
{
    private int timeLeft;
    public int timeLeftVal;
    public Slider timeSlider;
    public bool takingAway = false;
    public bool isTimeUp = false;
    public GameObject truck;
    private Animator truckAnim;

    public GameObject Spawner;
    public PoliceControl policeControl;
    public SaveSystem saveSystem;
    public ShopManager shopManager;

    public GameObject newsButton;
    public GameObject[] news;
    private int newsLength;
    //public bool isPaused;
    //public bool isTruckHere = false;

    // Start is called before the first frame update
    void Start()
    {
        // set up the animator variable
        timeSlider.maxValue = timeLeftVal;
        timeLeft = timeLeftVal;
        truckAnim = truck.GetComponent<Animator>();
        Spawner.SetActive(true);
        newsLength = news.Length;
    }

    // Update is called once per frame
    void Update()
    {
        // value of slider represents the timer
        timeSlider.value = timeLeft;
        // Return back to menu when press esc, for testing
        if (Input.GetKey(KeyCode.Escape))
        {
            SceneManager.LoadScene("MainMenu");
        }

        // Start the countdown timer
        if (takingAway == false)
        {
            if (!policeControl.isTimeStop)
            {
                StartCoroutine(TimerCount());
            }
            else
            {
                StopCoroutine(TimerCount());
            }
        }
        

        // truck comes and game paused when time up
        if (isTimeUp)
        {
            //truck.SetActive(true);
            //truckAnim.Play("TruckMoveIn");
            Spawner.SetActive(false);
            newsButton.SetActive(false);
            /*
            // pauses when finished the animation
            StartCoroutine(AfterAnimation(truckAnim.GetCurrentAnimatorStateInfo(0).length * 1.5f));
            if (isTruckHere)
            {
                isPaused = true;
            }
        }
        if (isPaused)
        {
            Time.timeScale = 0;
        }
        else
        {
            Time.timeScale = 1;
            isPaused = false;*/
        }
       
    }
    IEnumerator TimerCount()
    {
        takingAway = true;
        // start counting down
        yield return new WaitForSeconds(1);
        timeLeft -= 1;
        if (timeLeft == 0)
        {
            isTimeUp = true;
            //GetComponent<AudioSource>().Play();
            truckAnim.Play("TruckMoveIn");
            DestroyAll();
        }
        if (timeLeft != 0 && timeLeft % 20 == 0 && !isTimeUp)
        {
            Debug.Log("NewsOn");
            newsButton.SetActive(true);
        }
        takingAway = false;
    }

    // button function to reset the time and unpause
    public void ResetTime()
    {
        saveSystem.truckCount++;
        timeLeft = timeLeftVal;
        //isTruckHere = false;
        isTimeUp = false;
        Spawner.SetActive(true);
        //isPaused = false;
    }
    /*
    IEnumerator AfterAnimation(float _delay = 0)
    {
        yield return new WaitForSeconds(_delay);
        isTruckHere = true;
        yield return new WaitForSeconds(timeLeft);
        isTruckHere = false;
    }*/
    public void RemoveElement(ref GameObject[] array, int index)
    {
        for (int i = index; i < array.Length - 1; i++)
        {
            array[i] = array[i + 1];
        }
        Array.Resize(ref array, array.Length - 1);
    }

    public void ReadNews()
    {
        Time.timeScale = 0;
        news[Random.Range(0, newsLength)].gameObject.SetActive(true);
    }
    public void QuitNews()
    {
        Time.timeScale = 1;
        shopManager.ecoCoins += 100;
        for (int i = 0; i < newsLength; i++)
        {
            news[i].gameObject.SetActive(false);
        }
    }

    // Functions to stop and start timer
    public void timePause()
    {
        Time.timeScale = 0;
    }
    public void timeStart()
    {
        Time.timeScale = 1;
    }

    public void ReturnMenu()
    {
        SceneManager.LoadScene("MainMenu");
    }

    public void DestroyAll()
    {
        GameObject[] recyclables = GameObject.FindGameObjectsWithTag("recycled");
        foreach (GameObject r in recyclables)
        {
            Destroy(r);
        }
        GameObject[] collectables = GameObject.FindGameObjectsWithTag("collectioned");
        foreach (GameObject c in collectables)
        {
            Destroy(c);
        }
        GameObject[] compostables = GameObject.FindGameObjectsWithTag("composted");
        foreach (GameObject p in compostables)
        {
            Destroy(p);
        }
        GameObject[] groundables = GameObject.FindGameObjectsWithTag("grounded");
        foreach (GameObject g in groundables)
        {
            Destroy(g);
        }
        GameObject[] trashables = GameObject.FindGameObjectsWithTag("trashed");
        foreach (GameObject t in trashables)
        {
            Destroy(t);
        }
    }
}
