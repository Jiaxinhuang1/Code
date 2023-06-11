using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Spawner : MonoBehaviour
{

	public GameObject[] spawnables;
	public Transform[] spawnPoints;
	public int spawnDifficulty;
	public int med;
	public int hard;
	public int maxSpawn;
	private int spawns;
	private float spawnTimer = 1;
	private int rng;
	private int rngPont;
	private int totalMaxSpawn;
	private int spawnsDecrease = 1;

	public UIManager uiManager;

	public List<GameObject> spawnedItems = new List<GameObject>();
	public int itemIdx;

	// Start is called before the first frame update
	void Start()
    {
		totalMaxSpawn = maxSpawn;
    }

    // Update is called once per frame
    void Update()
    {

		hard = spawnables.Length;
		spawnTimer -= Time.deltaTime;
		if(spawnTimer < 0)
		{
			rng = Random.Range(0, spawnDifficulty);
			rngPont = Random.Range(0, spawnPoints.Length);
			GameObject thisItem = Instantiate(spawnables[rng], 
				spawnPoints[rngPont].position, 
				spawnables[rng].transform.rotation);
			spawnTimer = maxSpawn;
			spawns++;
			if(maxSpawn > 1 && spawns > spawnsDecrease)
			{
				spawns = 0;
				maxSpawn--;
				spawnsDecrease++;
			}
			// Add the spawned items to a list
			spawnedItems.Add(thisItem);
			
		}
		if (itemIdx < 0)
        {
			itemIdx = 0;
        }
		// Moving along the list of items
		if (spawnedItems.Count != 0)
		{
			if (Input.GetKeyDown(KeyCode.X))
			{
				//Debug.Log(spawnedItems[itemIdx]);
				if (itemIdx + 1 > spawnedItems.Count - 1)
				{
					itemIdx = 0;
				}
				else
				{
					itemIdx += 1;
				}
			}
			if (Input.GetKeyDown(KeyCode.Z))
			{
				//Debug.Log(spawnedItems[itemIdx]);
				if (itemIdx - 1 < 0)
				{
					itemIdx = spawnedItems.Count - 1;
				}
				else
				{
					itemIdx -= 1;
				}
			}
		}
		if (spawnedItems.Count == 1)
        {
			itemIdx = 0;
        }
		//spawnedItems[itemIdx].gameObject.GetComponent<dragger>().isActive = true;
	}

	public void Reset()
	{
		maxSpawn = totalMaxSpawn - 2;
		spawnTimer = maxSpawn;
		spawns = 0;
		spawnsDecrease = 1;
		if(spawnDifficulty == med || spawnDifficulty == hard || spawnDifficulty == spawnables.Length)
		{
			spawnDifficulty = spawnables.Length;
		}
		else
		{
			spawnDifficulty = med;
		}
		
		// Creates and destroys a new array of litter objects (items that hit the ground)
		GameObject[] litter;
		litter = GameObject.FindGameObjectsWithTag("grounded");
		for (int i = 0; i < litter.Length; i ++)
		{
			Destroy(litter[i].gameObject);
		}
	}

	public void BuyRecycleCup()
	{
		uiManager.RemoveElement(ref spawnables, 0);
	}
}
