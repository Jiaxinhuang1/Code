using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class dragger : MonoBehaviour
{

	private float mouseX;
	private float mouseY;
	private float screenFactor;
	private float screenFactorY;

	public bool cancrush;
	public bool recycleable;
	public bool compostable;
	public bool trashable;
	public bool collectionable;
	private bool done;
	private bool crushed;

	public int objectPoints;


	private string sceneName;

	public List<GameObject> spawnedItems;
	private int itemIdx;
	private GameObject focusItem;
	private GameObject spawnerObject;
	private Spawner spawner;
	private bool isActive = true;
	private bool updated = false;
	private bool popupDone = false;
	

	// Start is called before the first frame update
	void Start()
	{
		screenFactor = 10.5f / Screen.width;
		screenFactorY = 6f / Screen.height;
		sceneName = SceneManager.GetActiveScene().name;
		itemIdx = 0;
		spawnerObject = GameObject.FindGameObjectWithTag("spawner");
		spawner = spawnerObject.GetComponent<Spawner>();

		Debug.Log(SystemInfo.deviceType);
		//Debug.Log(sceneName);
	}

	// Update is called once per frame
	void Update()
	{
		//GetComponent<Rigidbody>().AddForce(Vector3.up * Time.deltaTime * 400);
		// when object is crushed, move object along conveyor belt (no gravity)
		if (crushed)
        {
			GetComponent<Rigidbody>().useGravity = false;
			GetComponent<Rigidbody>().isKinematic = true;
			transform.position = new Vector3(transform.position.x - 0.025f, transform.position.y, transform.position.z);

        }
		/*
		// Start Attempt on Tetris style gameplay
		// Get the list created from Spawner script
		spawnedItems = spawnerObject.GetComponent<Spawner>().spawnedItems;
		// Tetris Style mechanic only if this is not on mobile
		if (SystemInfo.deviceType != DeviceType.Handheld)
		{
			// If it hits the bins or the ground, remove it from list and deactivate it
			if (this.gameObject.tag != "item")
			{
				spawnerObject.GetComponent<Spawner>().spawnedItems.Remove(this.gameObject);
				this.isActive = false;
				GetComponent<Cromos.OutlineTarget>().enabled = false;
				// Since object deleted the itemIdx should decrease to have same object activated
				if (!updated)
				{
					if (spawner.spawnedItems.Count > 0 )
					{
						spawner.itemIdx -= 1;
					}
					else
					{
						spawner.itemIdx = 0;
					}
					updated = true;
				}
			}
			// Can only be set active if there is at least one item in the spawnedItems list
			if (spawner.itemIdx < spawnedItems.Count && spawner.spawnedItems.Count > 0)
			{
				if (spawner.itemIdx < spawnedItems.Count && this.gameObject != spawner.spawnedItems[spawner.itemIdx])
				{
					this.isActive = false;
					GetComponent<Cromos.OutlineTarget>().enabled = false;
				}

				// can move item only if it is activated one at a time
				if (spawner.itemIdx < spawnedItems.Count && this.gameObject == spawner.spawnedItems[spawner.itemIdx])//(this.isActive && this.gameObject == spawnedItems[0])
				{
					// Use arrow keys to move items
					if (Input.GetKey(KeyCode.LeftArrow))
					{
						if (transform.position.x > -4f)
						{
							transform.position += new Vector3(-0.04f, 0, 0);
						}
						else
						{
							transform.position += new Vector3(0, 0, 0);
						}
					}
					else if (Input.GetKey(KeyCode.RightArrow))
					{
						if (transform.position.x < 4f)
						{
							transform.position += new Vector3(0.04f, 0, 0);
						}
						else
						{
							transform.position += new Vector3(0, 0, 0);
						}
					}
					else if (Input.GetKey(KeyCode.DownArrow))
					{
						transform.position += new Vector3(0, -0.04f, 0);
					}
					GetComponent<Cromos.OutlineTarget>().enabled = true;
				}
			}
		}
		*/
	}

	// no gravity on item when mouse click
	private void OnMouseDown()
	{
		GetComponent<Rigidbody>().useGravity = false;
		GetComponent<Rigidbody>().isKinematic = true;
		mouseX = Input.mousePosition.x;
		mouseY = Input.mousePosition.y;
		GetComponent<Cromos.OutlineTarget>().enabled = true;
	}

	// gravity return when mouse release
	private void OnMouseUp()
	{
		GetComponent<Rigidbody>().useGravity = true;
		GetComponent<Rigidbody>().isKinematic = false;
		GetComponent<Cromos.OutlineTarget>().enabled = false;
	}

	// object move with mouse drag
	private void OnMouseDrag()
	{
		float mouseChange = screenFactor * (Input.mousePosition.x - mouseX);
		float mouseChangeY = screenFactorY * (Input.mousePosition.y - mouseY);
		transform.Translate(
			new Vector3(mouseChange, mouseChangeY, 0), Space.World);
		mouseX = Input.mousePosition.x;
		mouseY = Input.mousePosition.y;
	}

	// Triggers when object collides with bins, crusher, or ground
	private void OnTriggerEnter(Collider other)
	{
		// When hit crusher, decrease scale
		if (other.tag == "crush" && cancrush)
		{
			cancrush = false;
			GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Recycling(Mathf.RoundToInt(objectPoints/2));
			if (!popupDone)
			{
				GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
				popup.GetComponentInChildren<Text>().text = "+" + Mathf.RoundToInt(objectPoints/2).ToString();
				popupDone = true;
				Destroy(popup, 2);
			}
			popupDone = false;
			if (GetComponent<AudioSource>() != null)
				GetComponent<AudioSource>().Play();
			transform.localScale = new Vector3(transform.localScale.x, transform.localScale.y * .1f, transform.localScale.z);
			other.GetComponentInChildren<Animator>().SetTrigger("crush");
			crushed = true;
		}
		// Object is moved alond conveyor belt in Update function until it hits the stop trigger
		if (other.tag == "stop" && crushed)
		{
			crushed = false;
			GetComponent<Rigidbody>().useGravity = true;
			GetComponent<Rigidbody>().isKinematic = false;
		}
		// When hit compost bin, decrease scale and increase compost points depending on scene
		if (other.tag == "compost" && !done)
		{
			if (compostable)
			{
				other.GetComponent<ParticleSystem>().Play();
				other.GetComponent<AudioSource>().Play();
				transform.localScale *= .6f;
				done = true;
				if (sceneName == "Austin")
				{
					GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Composting(objectPoints);
					// Triggers popup text once with the object points as text then destroy after 2 seconds
					if (!popupDone)
					{
						GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
						popup.GetComponentInChildren<Text>().text = "+" + objectPoints.ToString();
						popupDone = true;
						Destroy(popup, 2);
					}
				}
				// Object points multiplier depending on which scene you are in
				else if (sceneName == "Paris")
                {
					GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Composting(2 * objectPoints);
					if (!popupDone)
					{
						GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
						popup.GetComponentInChildren<Text>().text = "+" + (2 * objectPoints).ToString();
						popupDone = true;
						Destroy(popup, 2);
					}
				}
				else if (sceneName == "Mexico")
                {
					GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Composting(3 * objectPoints);
					if (!popupDone)
					{
						GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
						popup.GetComponentInChildren<Text>().text = "+" + (3 * objectPoints).ToString();
						popupDone = true;
						Destroy(popup, 2);
					}
				}

			}
			else
			{
				GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Littering(objectPoints);
				if (!popupDone)
				{
					GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
					popup.GetComponentInChildren<Text>().text = "-" + objectPoints.ToString();
					popupDone = true;
					Destroy(popup, 2);
					GetComponent<AudioSource>().Play();
				}
			}
		}
		// When hit recycle bin, decrease scale and increase recycle points depending on scene
		if (other.tag == "recycle" && !done)
		{

			if (recycleable)
			{
				other.GetComponent<ParticleSystem>().Play();
				other.GetComponent<AudioSource>().Play();
				transform.localScale *= .6f;
				done = true;
				if (sceneName == "Austin")
				{
					GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Recycling(objectPoints);
					if (!popupDone)
					{
						GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
						popup.GetComponentInChildren<Text>().text = "+" + objectPoints.ToString();
						popupDone = true;
						Destroy(popup, 2);
					}
				}
				else if (sceneName == "Paris")
                {
					GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Recycling(2 * objectPoints);
					if (!popupDone)
					{
						GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
						popup.GetComponentInChildren<Text>().text = "+" + (2 * objectPoints).ToString();
						popupDone = true;
						Destroy(popup, 2);
					}
				}
				else if (sceneName == "Mexico")
                {
					GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Recycling(3 * objectPoints);
					if (!popupDone)
					{
						GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
						popup.GetComponentInChildren<Text>().text = "+" + (3 * objectPoints).ToString();
						popupDone = true;
						Destroy(popup, 2);
					}
				}

			}
			else
			{
				GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Littering(objectPoints);
				if (!popupDone)
				{
					GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
					popup.GetComponentInChildren<Text>().text = "-" + objectPoints.ToString();
					popupDone = true;
					Destroy(popup, 2);
					GetComponent<AudioSource>().Play();
				}

			}
		}
		// When hit collection bin, decrease scale and increase collection points depending on scene
		if (other.tag == "collection" && !done)
		{
			if (collectionable)
			{
				other.GetComponent<ParticleSystem>().Play();
				other.GetComponent<AudioSource>().Play();
				transform.localScale *= .6f;
				done = true;
				if (sceneName == "Austin")
				{
					GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Collectioning(objectPoints);
					if (!popupDone)
					{
						GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
						popup.GetComponentInChildren<Text>().text = "+" + objectPoints.ToString();
						popupDone = true;
						Destroy(popup, 2);
					}
				}
				else if (sceneName == "Paris")
                {
					GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Collectioning(2 * objectPoints);
					if (!popupDone)
					{
						GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
						popup.GetComponentInChildren<Text>().text = "+" + (2 * objectPoints).ToString();
						popupDone = true;
						Destroy(popup, 2);
					}
				}
				else if (sceneName == "Mexico")
                {
					GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Collectioning(3 * objectPoints); if (!popupDone)
					{
						GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
						popup.GetComponentInChildren<Text>().text = "+" + (3 * objectPoints).ToString();
						popupDone = true;
						Destroy(popup, 2);

					}
				}
			}
			else
			{
				GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Littering(objectPoints);
				if (!popupDone)
				{
					GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, Quaternion.identity) as GameObject;
					popup.GetComponentInChildren<Text>().text = "-" + objectPoints.ToString();
					popupDone = true;
					Destroy(popup, 2);
					GetComponent<AudioSource>().Play();

				}
			}
		}

		// When hit ground, increase litter score
		if (other.tag == "litter")
		{
			//GameObject.FindGameObjectWithTag("litterbug").GetComponent<Animator>().SetTrigger("litterbug");
			GameObject.FindGameObjectWithTag("score").GetComponent<ScoreKeeper>().Littering(objectPoints);
			Debug.Log("LitterBug!");
			other.GetComponentInParent<AudioSource>().Play();
			// other.GetComponent<AudioSource>().Play();
		}

		if (other.tag == "trash" && !done)
		{
			if (trashable)
			{
				other.GetComponent<ParticleSystem>().Play();
				other.GetComponent<AudioSource>().Play();
				transform.localScale *= .6f;
				done = true;
				if (!popupDone)
				{
					GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, other.transform.rotation) as GameObject;
					popup.GetComponentInChildren<Text>().text = "+0";
					popupDone = true;
				}
			}
			else
			{
				if (!popupDone)
				{
					GameObject popup = Instantiate(Resources.Load("NumFeedbackCanvas"), other.transform.position, other.transform.rotation) as GameObject;
					popup.GetComponentInChildren<Text>().text = "+0";
					popupDone = true;
					Destroy(popup, 2);
					GetComponent<AudioSource>().Play();
				}
			}
		}
	}
	// When hit ground or ground item, it becomes a litter
	public void OnCollisionEnter(Collision collision)
	{
		if (collision.collider.tag == "grounded" || collision.collider.tag == "ground")
		{
			this.tag = "grounded";
		}
	}

}
