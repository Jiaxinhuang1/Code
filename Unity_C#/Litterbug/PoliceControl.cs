using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PoliceControl : MonoBehaviour
{
    public ShopManager shopManager;
    public SaveSystem saveSystem;
    public ScoreKeeper scoreKeeper;
    public UIManager uiManager;
    public GameObject policeTicket;
    public GameObject jailBars;
    public bool isTimeStop = false;
    public bool done = false;

    private Animator ticketAnim;
    private Animator jailAnim;
    private Text ticketText;
    [SerializeField] private int litterCount;

    public GameObject spawner;
    // Start is called before the first frame update
    void Start()
    {
        ticketAnim = policeTicket.GetComponent<Animator>();
        jailAnim = jailBars.GetComponent<Animator>();
        ticketText = policeTicket.GetComponentInChildren<Text>();
        policeTicket.SetActive(false);

    }

    // Update is called once per frame
    void Update()
    {
        GameObject[] groundItems = GameObject.FindGameObjectsWithTag("grounded");
        litterCount = groundItems.Length;
        if (uiManager.isTimeUp == false)
        {
            if (scoreKeeper.ticketAmount == 1 || scoreKeeper.ticketAmount == 3 || scoreKeeper.ticketAmount == 5)
            {
                done = false;
            }
            if (scoreKeeper.ticketAmount == 2 && !done)
            {
                ticketText.text = "First Warning... DO NOT LITTER";
                policeTicket.SetActive(true);
                done = true;
                //ticketAnim.Play("GetTicketAnim");
                //Invoke(nameof(ResetAnim), 3f);
                //GetComponent<AudioSource>().Play();
            }
            if (scoreKeeper.ticketAmount == 4 && !done)
            {
                ticketText.text = "Second Warning... You better Watch Out!";
                policeTicket.SetActive(true);
                done = true;
                //Invoke(nameof(ResetAnim), 3f);
                //ticketAnim.SetTrigger("JailArrest");
                //ticketAnim.Play("GetTicketAnim");
                //GetComponent<AudioSource>().Play();
            }
            if (scoreKeeper.ticketAmount == 6 && !done)
            {
                jailAnim.Play("JailArrestAnim");
                spawner.SetActive(false);
                isTimeStop = true;
                done = true;
                //Invoke(nameof(ResetAnim), 3f);
            }
        }
    }

    public void PayFine()
    {
        saveSystem.arrestCount++;
        shopManager.ecoCoins = Mathf.RoundToInt(shopManager.ecoCoins / 2);
        scoreKeeper.ticketAmount = 0;
        jailAnim.Play("JailOutAnim");
        spawner.SetActive(true);
        isTimeStop = false;
        done = false;
        uiManager.DestroyAll();
    }

    private void ResetAnim()
    {
        // Resets the Animation so it can be replayed
        //policeTicket.GetComponent<Animator>().Play("GetTicketAnim", 0, 0);
        done = false;

    }
}
