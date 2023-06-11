using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ShopManager : MonoBehaviour
{
    public ScoreKeeper scoreKeeper;
    public PoliceControl policeControl;

    public int ecoCoins;

    public bool hasBigTrashBin;
    public bool hasBigRecycleBin;
    public bool hasCrusher;
    public bool hasCompost;
    public bool hasCollection;

    private GameObject trashBin;
    private GameObject recycleBin;
    private GameObject crusher;
    private GameObject collectionBin;
    private GameObject compostBin;
    private GameObject crushStand;

    public bool travelMexico;
    public bool travelParis;
    public bool travelAustin;


    // Start is called before the first frame update
    void Start()
    {
        travelAustin = true;

        trashBin = GameObject.FindGameObjectWithTag("trash");
        recycleBin = GameObject.FindGameObjectWithTag("recycle");
        crusher = GameObject.FindGameObjectWithTag("crush");
        collectionBin = GameObject.FindGameObjectWithTag("collection");
        compostBin = GameObject.FindGameObjectWithTag("compost");
        crushStand = GameObject.FindGameObjectWithTag("crushstand");
    }

    // Update is called once per frame
    void Update()
    {
        if (ecoCoins < 0)
        {
            ecoCoins = 0;
        }
        // Change the text object with ecoCoins tag to change with ecoCoin value
        GameObject[] ecoCoinTexts;
        ecoCoinTexts = GameObject.FindGameObjectsWithTag("ecoCoins");
        foreach (GameObject ecoCoin in ecoCoinTexts)
        {
            ecoCoin.GetComponent<Text>().text = ecoCoins.ToString();
        }

        // Increase scale of trash bin when player buys the bigger trash bin
        if (hasBigTrashBin)
        {
            trashBin.transform.localScale = new Vector3(0.8f, 0.9f , 0.8f);
        }
        else
        {
            trashBin.transform.localScale = new Vector3(0.6f, 0.7f, 0.6f);
        }
        // Increase scale of recycle bin when player buys the bigger recycle bin
        if (hasBigRecycleBin)
        {
            recycleBin.transform.localScale = new Vector3(1, 0.7f, 1);
        }
        else
        {
            recycleBin.transform.localScale = new Vector3(0.7f, 0.5f, 1);
        }

        // Set bin active when item is bought else set it inactive
        if (hasCrusher)
        {
            crusher.SetActive(true);
            crushStand.SetActive(true);
        }
        else
        {
            crusher.SetActive(false);
            crushStand.SetActive(false);
        }
        if (hasCompost)
        {
            compostBin.SetActive(true);
        }
        else
        {
            compostBin.SetActive(false);
        }
        if (hasCollection)
        {
            collectionBin.SetActive(true);
        }
        else
        {
            collectionBin.SetActive(false);
        }
    }

    // Functions to buy items on button click
    public void BuyBigTrash()
    {
        hasBigTrashBin = true;
    }

    public void BuyBigRecycle()
    {
        hasBigRecycleBin = true;
    }

    public void BuyCompost()
    {
        hasCompost = true;
    }

    public void BuyCollection()
    {
        hasCollection = true;
    }

    public void BuyCrusher()
    {
        hasCrusher = true;
    }

    public void BuyTicketExcuse()
    {
        scoreKeeper.ticketAmount -= 2;
    }

    public void BuyParis()
    {
        travelParis = true;
    }

    public void BuyMexico()
    {
        travelMexico = true;
    }

}
