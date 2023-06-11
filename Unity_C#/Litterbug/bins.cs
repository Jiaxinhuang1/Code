using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bins : MonoBehaviour
{

	public string binType;

	private void Start()
	{
		
	}

	private void OnTriggerEnter(Collider other)
	{
		other.tag = binType;
	}

	public void EmptyBin()
	{
		GetComponent<ParticleSystem>().Play();
		GetComponent<AudioSource>().Play();
		GameObject[] allInBin = GameObject.FindGameObjectsWithTag(binType);
		foreach(GameObject t in allInBin)
		{
			Destroy(t);
		}
	}
}
