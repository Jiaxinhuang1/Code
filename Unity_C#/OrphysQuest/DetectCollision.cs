using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DetectCollision : MonoBehaviour
{
    public GameObject ball;
    public static int herbsCount;
    public Text herbText;
    public static int healthCount = 100;
    public Text healthText;
    public static int killedCount;
    public Text killedText;
    public static int keyCount;
    public Text keyText;
    public static int appleCount;
    public Text applesText;
    public static int moneyCount = 100;
    public Text moneyText;

    public Text notificationText;

    public AudioSource questComplete;

    private bool isPlayed = false;
    private bool isPlayedTwo = false;
    private bool isPlayedThree = false;
    private bool isPlayedFour = false;

    public AudioSource pickUpSound;
    public AudioSource throwSound;

    public GameObject winPanel;

    public GameObject losePanel;

    private float timeBetweenAttacks = 0.65f;
    bool alreadyAttacked;
    // Start is called before the first frame update
    void Start()
    {
        losePanel.SetActive(false);
        winPanel.SetActive(false);
    }
    private void ResetAttack()
    {
        alreadyAttacked = false;
    }

    // Update is called once per frame
    void Update()
    { 

        if (Input.GetMouseButtonDown(0))
        {
            if (!alreadyAttacked)
            {
                Instantiate(throwSound);
                GameObject newBullet = Instantiate(ball as GameObject, transform.position + Vector3.up * 0.25f, transform.rotation);
                newBullet.GetComponent<Rigidbody>().velocity = transform.forward * 30;
                alreadyAttacked = true;
                Invoke(nameof(ResetAttack), timeBetweenAttacks);
            }
        }
        herbText.text = "Mushrooms: " + herbsCount + "/" + DialogueQuest.requiredHerbs;
        healthText.text = "Health: " + healthCount;
        killedText.text = "Goblin bodies: " + killedCount + "/" + DialogueQuest.requiredKills;
        applesText.text = "Apples: " + appleCount + "/" + DialogueQuest.requiredApples;
        moneyText.text = "Money:  " + moneyCount;
        keyText.text = "Keys: " + keyCount + "/" + DialogueQuest.requiredKeys;

        //changing UI text for herbs quest
        if(DialogueQuest.herbQuestActive)
        {
            herbText.color = Color.white;
        }
        if (DialogueQuest.herbQuestCompleted)
        {
            herbText.enabled = false;
        }
        if (herbsCount >= DialogueQuest.requiredHerbs)
        {
            herbText.color = Color.gray;
            if (isPlayedTwo == false)
            {
                Instantiate(questComplete);
                isPlayedTwo = true;
            }
        }
        //changing UI text of killed enemies
        if (DialogueQuest.killQuestActive)
        {
            killedText.color = Color.white;
        }
        if (DialogueQuest.killQuestCompleted)
        {
            killedText.enabled = false;
        }
        if (killedCount >= DialogueQuest.requiredKills)
        {
            killedText.color = Color.gray;
            if (isPlayedThree == false)
            {
                Instantiate(questComplete);
                isPlayedThree = true;
            }
        }
        //changing UI text of keys
        if (DialogueQuest.keyQuestActive)
        {
            keyText.color = Color.white;
        }
        if (DialogueQuest.keyQuestCompleted)
        {
            keyText.enabled = false;
        }
        if (keyCount >= DialogueQuest.requiredKeys)
        {
            keyText.color = Color.gray;
            if (isPlayedFour == false)
            {
                Instantiate(questComplete);
                isPlayedFour = true;
            }
        }
        //changing UI text of apple 
        if (DialogueQuest.appleQuestActive)
        {
            applesText.color = Color.white;
        }
        if (appleCount >= DialogueQuest.requiredApples)
        {
            applesText.color = Color.gray;
            if (isPlayed == false)
            {
                Instantiate(questComplete);
                isPlayed = true;
            }
        }
        if(DialogueQuest.appleQuestCompleted)
        {
            applesText.enabled = false;
        }

        if(healthCount <= 0)
        {
            losePanel.SetActive(true);
            Time.timeScale = 0;
        }
    }
    void OnTriggerEnter(Collider other)
    {
        if(other.gameObject.tag == "herbs")
        {
            if (DialogueQuest.herbQuestActive == true || DialogueQuest.herbQuestCompleted ==true)
            {
                herbsCount += 1;
                Instantiate(pickUpSound);
                Destroy(other.gameObject);
            } 
            else
            {
                notificationText.text = "Your quest is not active. Talk to village NPC to activate the quest";
            }
            
        }
        if (other.gameObject.tag == "key")
        {
            if (DialogueQuest.keyQuestActive == true || DialogueQuest.keyQuestCompleted == true)
            {
                Instantiate(pickUpSound);
                keyCount += 1;
                Destroy(other.gameObject);
            }
            else
            {
                notificationText.text = "Your quest is not active. Talk to village NPC to activate your quest";
            }

        }
        if (other.gameObject.tag == "dadNPC")
        {
            winPanel.SetActive(true);
            Time.timeScale = 0;
        }
        if (other.gameObject.tag == "death")
        {
            if (DialogueQuest.killQuestActive == true || DialogueQuest.killQuestCompleted == true)
            {
                Instantiate(pickUpSound);
                killedCount += 1;
                Destroy(other.gameObject);
            }
            else
            {
                notificationText.text = "Your quest is not active. Talk to village NPC to activate your quest";
            }

        }

    }
    public void OnCollisionEnter(Collision collision)
    {
        if (collision.collider.tag == "apple")
        {
            if (DialogueQuest.appleQuestActive == true || DialogueQuest.appleQuestCompleted == true)
            {
                Instantiate(pickUpSound);
                appleCount += 1;
                Destroy(collision.gameObject);
            }
            else
            {
                notificationText.text = "Your quest is not active. Talk to village NPC to activate your quest";
            }

        }


    }
    public void OnTriggerExit(Collider other)
    {
        if(other.gameObject.tag == "herbs" || other.gameObject.tag == "key" || other.gameObject.tag == "apple" || other.gameObject.tag == "death")
        {
            notificationText.text = "";
        }

    }
    public void OnCollisionExit(Collision collision)
    {
        if(collision.collider.tag == "apple")
        {
            notificationText.text = "";
        }
    }
}
