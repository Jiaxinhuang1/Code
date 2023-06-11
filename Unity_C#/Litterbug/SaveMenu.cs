using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SaveMenu : MonoBehaviour
{
    public int hasBiggerBin;
    public int sortedAmt;
    public int legendCompost;
    public int hasParisUnlock;
    public int hasMexicoUnlock;
    public int arrestCount;
    public int truckCount;

    public Text bigBinText;
    public Text sortText;
    public Text compostText;
    public Text parisText;
    public Text mexicoText;
    public Text arrestText;
    public Text truckText;

    public GameObject bigBinAchieved;
    public GameObject sortAchieved;
    public GameObject compostAchieved;
    public GameObject parisAchieved;
    public GameObject mexicoAchieved;
    public GameObject arrestAchieved;
    public GameObject truckAchieved;
    

    // Start is called before the first frame update
    void Start()
    {
        hasBiggerBin = PlayerPrefs.GetInt("hasBigRecycle");
        sortedAmt = PlayerPrefs.GetInt("sortedItems");
        legendCompost = PlayerPrefs.GetInt("legendaryComposer");
        hasParisUnlock = PlayerPrefs.GetInt("hasParis");
        hasMexicoUnlock = PlayerPrefs.GetInt("hasMexico");
        arrestCount = PlayerPrefs.GetInt("arrest");
        truckCount = PlayerPrefs.GetInt("truck");

    }

    // Update is called once per frame
    void Update()
    {
        bigBinText.text = hasBiggerBin.ToString();
        sortText.text = sortedAmt.ToString();
        compostText.text = legendCompost.ToString();
        parisText.text = hasParisUnlock.ToString();
        mexicoText.text = hasMexicoUnlock.ToString();
        arrestText.text = arrestCount.ToString();
        truckText.text = truckCount.ToString();

        if (hasBiggerBin == 1)
        {
            bigBinAchieved.SetActive(true);
        }
        else
        {
            bigBinAchieved.SetActive(false);
        }
        if (sortedAmt == 100)
        {
            sortAchieved.SetActive(true);
        }
        else
        {
            sortAchieved.SetActive(false);
        }
        if (legendCompost == 500)
        {
            compostAchieved.SetActive(true);
        }
        else
        {
            compostAchieved.SetActive(false);
        }
        if (hasParisUnlock == 1)
        {
            parisAchieved.SetActive(true);
        }
        else
        {
            parisAchieved.SetActive(false);
        }
        if (hasMexicoUnlock == 1)
        {
            mexicoAchieved.SetActive(true);
        }
        else
        {
            mexicoAchieved.SetActive(false);
        }
        if (arrestCount == 3)
        {
            arrestAchieved.SetActive(true);
        }
        else
        {
            arrestAchieved.SetActive(false);
        }
        if (truckCount == 3)
        {
            truckAchieved.SetActive(true);
        }
        else
        {
            truckAchieved.SetActive(false);
        }

        if (Input.GetKeyDown("p"))
        {
            Debug.Log("Resetted Data");
            ResetData();
        }
    }
    public void ResetData()
    {
        hasBiggerBin = 0;
        sortedAmt = 0;
        legendCompost = 0;
        hasParisUnlock = 0;
        hasMexicoUnlock = 0;
        arrestCount = 0;
        truckCount = 0;
        PlayerPrefs.SetInt("hasBigRecycle", hasBiggerBin);
        PlayerPrefs.SetInt("sortedItems", sortedAmt);
        PlayerPrefs.SetInt("legendaryComposer", legendCompost);
        PlayerPrefs.SetInt("hasParis", hasParisUnlock);
        PlayerPrefs.SetInt("hasMexico", hasMexicoUnlock);
        PlayerPrefs.SetInt("arrest", arrestCount);
        PlayerPrefs.SetInt("truck", truckCount);
    }
}
