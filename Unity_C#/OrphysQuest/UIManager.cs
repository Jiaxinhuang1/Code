using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class UIManager : MonoBehaviour
{
    private void Start()
    {
        Time.timeScale = 1;
        DialogueQuest.appleQuestActive = false;
        DialogueQuest.appleQuestCompleted = false;
        DialogueQuest. turnAppleIn = false;
        DialogueQuest.killQuestActive = false;
        DialogueQuest.killQuestCompleted = false;
        DialogueQuest.turnKillIn = false;
        DialogueQuest.keyQuestActive = false;
        DialogueQuest.keyQuestCompleted = false;
        DialogueQuest.turnKeyIn = false;
        DialogueQuest.herbQuestActive = false;
        DialogueQuest.herbQuestCompleted = false;
        DialogueQuest.turnHerbsIn = false;
    }
    public void RestartLevel()
    {
        SceneManager.LoadScene("RevisedWhitebox");
        DetectCollision.healthCount = 100;
        DetectCollision.moneyCount = 100;
        DetectCollision.killedCount = 0;
        DetectCollision.herbsCount = 0;
        DetectCollision.keyCount = 0;
        DetectCollision.appleCount = 0;
    }
    public void QuitGame()
    {
        Application.Quit();
    }
    public void ReturnMenu()
    {
        SceneManager.LoadScene("Menu");
        DetectCollision.healthCount = 100;
        DetectCollision.moneyCount = 100;
        DetectCollision.killedCount = 0;
        DetectCollision.herbsCount = 0;
        DetectCollision.keyCount = 0;
        DetectCollision.appleCount = 0;
    }
}
