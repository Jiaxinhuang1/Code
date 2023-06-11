using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class ScoreKeeper : MonoBehaviour
{

	public Text recycled;
	public Text composted;
	public Text litter;
	public Text collection;
	public Text score;

	public Text recycledStat;
	public Text compostedStat;
	public Text litterStat;
	public Text collectionStat;
	public Text scoreStat;

	public int ticketAmount;

	//public GameObject ResetButton;

	//public GameObject giveUpButton;

	private int totalRecycled;
	private int totalComposted;
	private int totalLitter;
	private int totalCollection;
	private int totalScore;

	public bool hasTwoTimesPoints = false;
	public GameObject spawner;

	[SerializeField] private int litterCount;

	private int currentRecycled;
	private int currentComposted;

	public ShopManager shopManager;
	public SaveSystem saveSystem;
	public GameObject notification;
	public ObjectsInfo objectInfo;
	public PoliceControl policeControl;

	private bool hasTextPlayed = false;
    // Start is called before the first frame update
    void Start()
    {

    }

	void Update()
	{
		// ticket amount will be counted based on number of items on ground
		GameObject[] groundItems = GameObject.FindGameObjectsWithTag("grounded");
		litterCount = groundItems.Length;
		if (ticketAmount < 0)
		{
			ticketAmount = 0;
		}
		if (litterCount == 8 && ticketAmount == 0)
		{
			ticketAmount = 1;
		}
		if (litterCount == 15 && ticketAmount == 1)
        {
			ticketAmount = 2;
        }
		if (litterCount == 23 && ticketAmount == 2)
		{
			ticketAmount = 3;
		}
		if (litterCount == 30 && ticketAmount == 3)
		{
			ticketAmount = 4;
		}
		if (litterCount == 37 && ticketAmount == 4)
		{
			ticketAmount = 5;
		}
		if (litterCount == 45 && ticketAmount == 5)
		{
			ticketAmount = 6;
		}
		// 2x points starts only if player buys it and the spawner is active
		if (hasTwoTimesPoints && spawner.activeInHierarchy)
		{
			//Debug.Log("2X ON");
			Invoke(nameof(ResetTime), 15f);
			if (!hasTextPlayed)
			{
				notification.GetComponentInChildren<Text>().text = "2X Item Points Starts Now";
				notification.SetActive(true);
				hasTextPlayed = true;
			}
		}


	}

	public void Recycling(int objectPoints)
	{
		saveSystem.sortedAmt++;
		// When there is 2x points on, object points will count 2x more
		if (hasTwoTimesPoints)
		{
			totalRecycled += (2 * objectPoints);
			currentRecycled += objectPoints;
			if (objectInfo.recycleBoost > 0)
			{
				// If the incremental recycle boost is bought, object points will increase depending on how much you buy
				shopManager.ecoCoins += Mathf.RoundToInt(2 * objectPoints + (objectInfo.recycleBoost * objectPoints * 0.01f));
			}
			else
			{
				shopManager.ecoCoins += (2 * objectPoints);
			}
			CountScore();	// updates the value in text
		}
		else
		{
			totalRecycled += objectPoints;
			currentRecycled += objectPoints;
			if (objectInfo.recycleBoost > 0)
			{
				//Debug.Log("RecycleBoost: " + objectInfo.recycleBoost);
				shopManager.ecoCoins += Mathf.RoundToInt(objectPoints + (objectInfo.recycleBoost * objectPoints * 0.01f));
			}
			else
			{
				//Debug.Log("No Boost");
				shopManager.ecoCoins += objectPoints;
			}
			CountScore();
		}
	}
	public void Composting(int objectPoints)
	{
		saveSystem.sortedAmt++;
		saveSystem.legendCompost++;
		if (hasTwoTimesPoints)
		{
			totalComposted += (2 * objectPoints);
			currentComposted += objectPoints;
			shopManager.ecoCoins += (2 *objectPoints);
			CountScore();
		}
		else
		{
			totalComposted += objectPoints;
			currentComposted += objectPoints;
			shopManager.ecoCoins += objectPoints;
			CountScore();
		}
	}
	public void Collectioning(int objectPoints)
	{
		saveSystem.sortedAmt++;
		if (hasTwoTimesPoints)
		{
			totalCollection += (2 * objectPoints);
			shopManager.ecoCoins += (2 * objectPoints);
			CountScore();
		}
		else
		{
			totalCollection += objectPoints;
			shopManager.ecoCoins += objectPoints;
			CountScore();
		}
	}
	public void Littering(int objectPoints)
	{
		// Add half of points to litter and round to integer
		totalLitter += Mathf.RoundToInt(objectPoints / 2);
		//litterCount += Mathf.RoundToInt(objectPoints / 2);
		CountScore();
	}
	void CountScore()
	{
		// Update the text object with results from gameplay
		totalScore = totalRecycled + totalComposted - totalLitter;
		recycled.text = totalRecycled.ToString();
		composted.text = totalComposted.ToString();
		litter.text = totalLitter.ToString();
		collection.text = totalCollection.ToString();
		score.text = totalScore.ToString();

		recycledStat.text = totalRecycled.ToString();
		compostedStat.text = totalComposted.ToString();
		litterStat.text = totalLitter.ToString();
		collectionStat.text = totalCollection.ToString();
		scoreStat.text = totalScore.ToString();

		/*
		if(currentRecycled > 20 || currentComposted > 20)
		{
			currentComposted = 0;
			currentRecycled = 0;
			ResetButton.SetActive(true);
		}
		if(totalLitter > 20)
		{
			giveUpButton.SetActive(true);
		}*/
	}

	// called after 15 seconds to take down 2X time
	private void ResetTime()
	{
		hasTwoTimesPoints = false;
		if (hasTextPlayed)
		{
			notification.GetComponentInChildren<Text>().text = "2X Item points OFF";
			notification.SetActive(true);
			hasTextPlayed = false;
		}
		//Debug.Log("2X OFf");
	}
	// When bought the 2x points from shop activate the bool but does not start until get back to gameplay
	public void BuyTwoTimesPoints()
	{
		if (!hasTwoTimesPoints)
		{
			hasTwoTimesPoints = true;
		}
	}
	public void ResetScore()
	{
		totalScore = 0;
		totalRecycled = 0;
		totalComposted = 0;
		totalLitter = 0;
		totalCollection = 0;
	}

	public void GameOver()
	{
		SceneManager.LoadScene(1);
	}
}
