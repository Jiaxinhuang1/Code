using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class MenuManager : MonoBehaviour
{
    public GameObject loadConfirmationPanel;
    public GameObject changeEngPanel;
    public GameObject changeChinPanel;
    public GameObject howToPlayPanel;
    public GameObject englishButton;
    public GameObject chineseButton;

    [Header("Audio")]
    public AudioSource menuOpenSound;

    // Start is called before the first frame update
    void Start()
    {
        loadConfirmationPanel.transform.localScale = new Vector3(1, 0, 1);
        changeEngPanel.transform.localScale = new Vector3(1, 0, 1);
        changeChinPanel.transform.localScale = new Vector3(1, 0, 1);
        howToPlayPanel.transform.localScale = new Vector3(1, 0, 1);
        Debug.Log("Language: " + PlayerPrefs.GetString("Lang", "English"));
        if (PlayerPrefs.GetString("Lang") == "Chinese")
        {
            englishButton.SetActive(false);
            chineseButton.SetActive(true);
        }
        else
        {
            chineseButton.SetActive(false);
            englishButton.SetActive(true);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void OpenPanel(GameObject go)
    {
        LeanTween.scale(go, new Vector3(1, 1, 1), 0.2f);
        menuOpenSound.Play();
    }

    public void ClosePanel(GameObject go)
    {
        LeanTween.scale(go, new Vector3(1, 0, 1), 0.2f);
        menuOpenSound.Play();
    }

    public void LoadScene(string sceneName)
    {
        SceneManager.LoadScene(sceneName);
    }

    public void NewGame()
    {
        //PlayerPrefs.DeleteAll();
        PlayerPrefs.SetInt("ItemLevel", 1);
        PlayerPrefs.SetInt("TrashLevel", 0);
        PlayerPrefs.SetInt("RecycleLevel", 0);
        PlayerPrefs.SetInt("CompostLevel", 0);
        PlayerPrefs.SetInt("DifficultyLevel", 1);
    }

    public void ChangeLanguage(string lang)
    {
        PlayerPrefs.SetString("Lang", lang);
    }

}
