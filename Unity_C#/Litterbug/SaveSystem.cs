using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SaveSystem : MonoBehaviour
{
    public ScoreKeeper scoreKeeper;
    public ShopManager shopManager;
    public int hasBiggerBin;
    public int sortedAmt;
    public int legendCompost;
    public int hasParisUnlock;
    public int hasMexicoUnlock;
    public int arrestCount;
    public int truckCount;


    void Start()
    {
        hasBiggerBin = PlayerPrefs.GetInt("hasBigRecycle");
        sortedAmt = PlayerPrefs.GetInt("sortedItems");
        legendCompost = PlayerPrefs.GetInt("legendaryComposer");
        hasParisUnlock = PlayerPrefs.GetInt("hasParis");
        hasMexicoUnlock = PlayerPrefs.GetInt("hasMexico");
        arrestCount = PlayerPrefs.GetInt("arrest");
        truckCount = PlayerPrefs.GetInt("truck");

        if (hasParisUnlock == 1)
        {
            shopManager.travelParis = true;
        }
        else
        {
            shopManager.travelParis = false;
        }

        if (hasMexicoUnlock == 1)
        {
            shopManager.travelMexico = true;
        }
        else
        {
            shopManager.travelMexico = false;
        }
    }

    void Update()
    {
        if (shopManager.hasBigRecycleBin)
        {
            hasBiggerBin = 1;
        }
        if (hasBiggerBin >= 1)
        {
            hasBiggerBin = 1;
        }
        if (sortedAmt >= 100)
        {
            sortedAmt = 100;
        }
        if (legendCompost >= 500)
        {
            legendCompost = 500;
        }
        if (truckCount >= 3)
        {
            truckCount = 3;
        }
        if (arrestCount >= 3)
        {
            arrestCount = 3;
        }
        if (hasParisUnlock >= 1)
        {
            hasParisUnlock = 1;
        }
        if (hasMexicoUnlock >= 1)
        {
            hasMexicoUnlock = 1;
        }
        if (shopManager.travelParis)
        {
            hasParisUnlock = 1;
        }
        if (shopManager.travelMexico)
        {
            hasMexicoUnlock = 1;
        }
        SaveData();
        if (Input.GetKeyDown("p"))
        {
            Debug.Log("Resetted Data");
            ResetData();
        }
    }

    public void SaveData()
    {
        PlayerPrefs.SetInt("hasBigRecycle", hasBiggerBin);
        PlayerPrefs.SetInt("sortedItems", sortedAmt);
        PlayerPrefs.SetInt("legendaryComposer", legendCompost);
        PlayerPrefs.SetInt("hasParis", hasParisUnlock);
        PlayerPrefs.SetInt("hasMexico", hasMexicoUnlock);
        PlayerPrefs.SetInt("arrest", arrestCount);
        PlayerPrefs.SetInt("truck", truckCount);
    }

    public void ResetData()
    {
        //PlayerPrefs.DeleteAll();
        hasBiggerBin = 0;
        sortedAmt = 0;
        legendCompost = 0;
        hasParisUnlock = 0;
        hasMexicoUnlock = 0;
        arrestCount = 0;
        truckCount = 0;
        SaveData();
    }


}
