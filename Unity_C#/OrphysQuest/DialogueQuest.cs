using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DialogueQuest : MonoBehaviour
{
    public GameObject dialoguePanel;
    public Text dialogueText;

    public GameObject dadNPC;

    public static bool herbQuestActive = false;
    public static bool herbQuestCompleted = false;
    public static bool turnHerbsIn = false;
    public static int requiredHerbs = 15;

    public static bool killQuestActive = false;
    public static bool killQuestCompleted = false;
    public static bool turnKillIn = false;
    public static int requiredKills = 15;

    public static bool keyQuestActive = false;
    public static bool keyQuestCompleted = false;
    public static bool turnKeyIn = false;
    public static int requiredKeys = 3;

    public static bool appleQuestActive = false;
    public static bool appleQuestCompleted = false;
    public static bool turnAppleIn = false;
    public static int requiredApples = 10;

    public AudioSource questAccept;
    public AudioSource rewardPlayer;

    public GameObject allQuestCompleteText;
    private bool isDestroyed = false;


    // Start is called before the first frame update
    void Start()
    {
        allQuestCompleteText.SetActive(false);
        dialoguePanel.SetActive(false);
        dadNPC.SetActive(false);
    }

    private void Update()
    {
        if(turnAppleIn && turnKillIn && turnKeyIn && turnHerbsIn)
        {
            dadNPC.SetActive(true);
        }
        if(turnKeyIn && turnAppleIn && turnKillIn && turnHerbsIn && !isDestroyed)
        {
            allQuestCompleteText.SetActive(true);
            Destroy(allQuestCompleteText, 10);
            isDestroyed = true;
        }
    }

    // Update is called once per frame
    private void OnTriggerEnter(Collider other)
    {
        //Pick up herb quest system
        if(other.gameObject.tag == "herbNPC")
        {
            dialoguePanel.SetActive(true);
            herbQuestActive = true;
            Instantiate(questAccept);
            if (turnHerbsIn == false)
            {
                if (DetectCollision.herbsCount >= requiredHerbs)
                {
                    herbQuestCompleted = true;
                }
            }
            if(herbQuestCompleted == true)
            {
                dialogueText.text = "Oooo these mushrooms look nice and plump! Thank you!";
                herbQuestActive = false;
                if(turnHerbsIn == false)
                {
                    turnHerbsIn = true;
                    //reward the player
                    Instantiate(rewardPlayer);
                    DetectCollision.moneyCount += 150;
                    DetectCollision.herbsCount -= requiredHerbs;
                }
            }
            else
            {
                dialogueText.text = "Hey Orphy! Would you like to pick some mushrooms around the village and forest for me？ I am trying this new soup recipe for my husband. Don't worry. I will pay!";

            }
        }

        //Kill enemies quest system
        if (other.gameObject.tag == "killNPC")
        {
            dialoguePanel.SetActive(true);
            killQuestActive = true;
            Instantiate(questAccept);
            if (turnKillIn == false)
            {
                if (DetectCollision.killedCount >= requiredKills)
                {
                    killQuestCompleted = true;
                }
            }
            if (killQuestCompleted == true)
            {
                dialogueText.text = "Whaat! How did you kill them! What a courageous youngster. Here's your reward for your courageous act!";
                killQuestActive = false;
                if (turnKillIn == false)
                {
                    turnKillIn = true;
                    //reward the player
                    Instantiate(rewardPlayer);
                    DetectCollision.moneyCount += 200;
                    DetectCollision.killedCount -= requiredKills;
                }
            }
            else
            {
                dialogueText.text = "The goblins. Those terrifying creatures outside the forest. If only there was someone courageous enough to hunt them down. I can only rest in peace if I see those monstrous bodies.";

            }
        }

        //Find key quest system
        if (other.gameObject.tag == "keyNPC")
        {
            dialoguePanel.SetActive(true);
            keyQuestActive = true;
            Instantiate(questAccept);
            if (turnKeyIn == false)
            {
                if (DetectCollision.keyCount >= requiredKeys)
                {
                    keyQuestCompleted = true;
                }
            }
            if (keyQuestCompleted == true)
            {
                dialogueText.text = "You found my keys!?! Thank you so much! Here's some money. Go buy yourself anything!";
                keyQuestActive = false;
                if (turnKeyIn == false)
                {
                    turnKeyIn = true;
                    //reward the player
                    Instantiate(rewardPlayer);
                    DetectCollision.moneyCount += 50;
                    DetectCollision.keyCount -= requiredKeys;
                }
            }
            else
            {
                dialogueText.text = "Oh no! Where are my keys!?! I must've lost them when I went foraging in the forest.";

            }
        }
        //Hit tree for apple fall quest system
        if (other.gameObject.tag == "appleNPC")
        {
            dialoguePanel.SetActive(true);
            appleQuestActive = true;
            if (turnAppleIn == false)
            {
                Instantiate(questAccept);
                if (DetectCollision.appleCount >= requiredApples)
                {
                    appleQuestCompleted = true;
                }
            }
            if (appleQuestCompleted == true)
            {
                dialogueText.text = "Awww thank you dear! Feel free to come back to play around anytime!";
                appleQuestActive = false;
                if (turnAppleIn == false)
                {
                    turnAppleIn = true;
                    //reward the player
                    Instantiate(rewardPlayer);
                    DetectCollision.moneyCount += 75;
                    DetectCollision.appleCount -= requiredApples;
                }
            }
            else
            {
                dialogueText.text = "Urgh my back is hurting. Oh hey Orphy! Can you be a dear and pick some apples in the backyard for me? You might have to shoot the tree to make the apples fall.";

            }
        }
    }
    private void OnTriggerExit(Collider other)
    {
        if(other.gameObject.tag == "herbNPC" || other.gameObject.tag == "killNPC" || other.gameObject.tag == "keyNPC" || other.gameObject.tag == "appleNPC")
        {
            dialogueText.text = "";
            dialoguePanel.SetActive(false);
            //herbQuestActive = true;
        }

    }
}
