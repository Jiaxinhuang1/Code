using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerDetection : MonoBehaviour
{
    public Text haloKeeper;
    public int halo = 0;

    private float scoreTimer;
    public int score = 0;
    public Text scoreKeeper;

    private int health = 99;
    public Slider healthBar;

    public GameObject gameOverPanel;
    public GameObject pausePanel;

   // private bool scoreUp = false;
   // private bool haloUp = false;

    private float powerUpTimer;

    private PlayerMovement playerMovement;
    public LeaderBoadManager leaderBoardManager;
    public LevelGenerator levelGenerator;
    public CharacterSelect characterSelect;
    private bool respawned;
    private bool startRun;

    public GameObject respawnPanel;

    public AudioClip[] clipsSound;
    private AudioSource aS;

    // Start is called before the first frame update
    void Start()
    {
        respawned = false;
        startRun = true;
        playerMovement = this.GetComponent<PlayerMovement>();
        gameOverPanel.SetActive(false);
        pausePanel.SetActive(false);
        respawnPanel.SetActive(false);
        aS = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {
        //haloKeeper.text = halo.ToString("00");
       // scoreKeeper.text = score.ToString("0000");
        healthBar.value = health;
        if (playerMovement.start)
        {
            scoreTimer += Time.deltaTime;
        }
        // score Timer code. Adds a point every second. 
        if (scoreTimer>1f)
        { //checks if theres a power up on. If yes, adds 2 instead of one
            score += 1;

            scoreKeeper.text = score.ToString();
            scoreTimer = 0;
        }

        //if (this.gameObject.transform.position.y < -100f)
        //{
          //  gameOverPanel.SetActive(true);
        //}
        if (gameOverPanel.activeInHierarchy || pausePanel.activeInHierarchy || respawnPanel.activeInHierarchy || !startRun)
        {
            Time.timeScale = Mathf.Epsilon;
        }
        else
        {
            Time.timeScale = 1;
        }

        if (this.gameObject.transform.position.y < -60)
        {
            if (halo >= 15 && !respawned)
            {
                startRun = false;
                respawnPanel.SetActive(true);
            }
            else
            {
                GameOver();
            }
        }

    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.tag == "deathBox")
        {
            if (halo >= 15 && !respawned)
            {
                startRun = false;
                respawnPanel.SetActive(true);
                PlaySoundEffect(3);
            }
            else
            {
                PlaySoundEffect(3);
                GameOver();
            }
        }
        if (collision.tag == "trap")
        {
            health -= characterSelect.damage;
            PlaySoundEffect(2);
            if (health <= 1)
            {
                health = 0;
                leaderBoardManager.LoseGame();
                gameOverPanel.SetActive(true);
                
            }
        }
        if (collision.tag == "coin")
        {
          
            halo += characterSelect.haloIncrement;

            haloKeeper.text = halo.ToString();
            Destroy(collision.gameObject);
            PlaySoundEffect(0);
        }

        if (collision.tag == "Heal")
        {
            Debug.Log("HEAL PLZ");
            if (health + 20 >= 99)
            {
                health = 99;
                healthBar.value = health;
                PlaySoundEffect(1);
            }
            else
            {
                health += 20;
                healthBar.value = health;
                PlaySoundEffect(1);
            }
            Destroy(collision.gameObject);

        }
    }

    public void GameOver()
    {
        halo = 0;
        leaderBoardManager.LoseGame();
        gameOverPanel.SetActive(true);
        respawnPanel.SetActive(false);
        pausePanel.SetActive(false);
    }

    public void Respawn()
    {
        health = 100;
        halo -= 15;
        respawned = true;
        levelGenerator.Respawn();
        haloKeeper.text = halo.ToString();
    }

    public void StartRun()
    {
        startRun = true;
    }

    public void PlaySoundEffect(int index)
    {
        aS.PlayOneShot(clipsSound[index]);
    }
}
