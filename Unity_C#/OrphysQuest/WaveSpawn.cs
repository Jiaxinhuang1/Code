using UnityEngine;
using System.Collections;
public class WaveSpawn : MonoBehaviour {

	public int WaveSize;
	public GameObject EnemyPrefab;
	public float EnemyInterval;
	public Transform spawnPoint;
	public float startTime;
	//public Transform[] WayPoints;
	public static int enemyCount=0;

	void Start ()
    {


	}

	void Update()
	{
		/*if(enemyCount > WaveSize)
		{
			CancelInvoke("SpawnEnemy");
		}*/
		if (enemyCount < 1)
		{
			InvokeRepeating("SpawnEnemy", startTime, EnemyInterval);
		}
		else
		{
			CancelInvoke("SpawnEnemy");
		}
	}

	void SpawnEnemy()
	{
		enemyCount++;
		Debug.Log(enemyCount);
		GameObject enemy = GameObject.Instantiate(EnemyPrefab,spawnPoint.position,Quaternion.identity) as GameObject;
		//enemy.GetComponent<Enemy>().waypoints = WayPoints;
      
    }
}
