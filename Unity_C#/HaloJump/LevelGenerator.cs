using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LevelGenerator : MonoBehaviour
{
    private const float playerDistance = 200f;
    [SerializeField] private Transform levelPart_Start;
    [SerializeField] private List<Transform> levelPartEasyList;
    [SerializeField] private List<Transform> levelPartMedList;
    [SerializeField] private List<Transform> levelPartHardList;
    private List<Transform> difficultyLevelParts;
    [SerializeField] private Transform player;

    private Vector3 lastEndPosition;
    private int spawnedCount;

    public enum Difficulty
    {
        easy,
        medium,
        hard
    }


    private void Awake()
    {
        // Find where the first level part ends
        lastEndPosition = levelPart_Start.Find("EndPosition").position;
        // Instantiate 5 level parts at awake
        int startingParts = 2;
        for (int i=0; i <startingParts; i++)
        {
           SpawnLevelPart();
        }
    }

    private void Update()
    {
        // Spawn a level part if the distance between player position and end position is less than 200
        if (Vector3.Distance(player.position, lastEndPosition) < playerDistance)
        {
            SpawnLevelPart();
        }
    }

    private void SpawnLevelPart()
    {
        // switch the lists of spawned platforms based on the difficulty
        switch (GetDifficulty())
        {
            case Difficulty.easy:
                difficultyLevelParts = levelPartEasyList;
                break;
            case Difficulty.medium:
                difficultyLevelParts = levelPartMedList;
                break;
            case Difficulty.hard:
                difficultyLevelParts = levelPartHardList;
                break;
        }

        // Choose a level part randomly from the list and spawn it after the end position
        Transform chosenLevelPart = difficultyLevelParts[Random.Range(0, difficultyLevelParts.Count)];
        Transform lastLevelPartTransform = SpawnLevelPart(chosenLevelPart, lastEndPosition);
        // Update the end position
        lastEndPosition = lastLevelPartTransform.Find("EndPosition").position;
        spawnedCount++;
    }

    private Transform SpawnLevelPart(Transform levelPart, Vector3 spawnPosition)
    {
        Transform levelPartTransform = Instantiate(levelPart, spawnPosition, Quaternion.identity);
        return levelPartTransform;
    }

    private Difficulty GetDifficulty()
    {
        // change difficulty based on the amount of platforms spawned
        if (spawnedCount >= 6)
        {
            return Difficulty.hard;
        }
        else if (spawnedCount >= 3)
        {
            return Difficulty.medium;
        }
        else
        {
            return Difficulty.easy;
        }
        
    }

    public void Respawn()
    {
        player.transform.position = lastEndPosition - new Vector3(3, -2, 0);
    }
}
