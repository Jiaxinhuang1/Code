using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class JumpPad : MonoBehaviour
{
    // force can be changed in inspector
    public float jumpForce = 10f;
    public float diagonalJump = 10f;
    public AudioSource JumpPadSound;

    void start()  
    {
        JumpPadSound = GetComponent<AudioSource>();
    }
    void OnCollisionEnter(Collision collision)      
    {
        // jump high when gameobject with player tag collides with the jumppad (gameobject with this script)
        if (collision.collider.gameObject.CompareTag("Player") |
        collision.collider.gameObject.CompareTag("Robot") |
        collision.collider.gameObject.CompareTag("Alien"))
        {
            //relativeforce is less intensive, pushes player in direction they are facing(good for multiplayer)
            collision.collider.gameObject.GetComponent<Rigidbody>().AddRelativeForce(Vector3.up * jumpForce, ForceMode.Impulse);
            //collision.collider.gameObject.GetComponent<Rigidbody>().AddRelativeForce(Vector3.forward * jumpForce, ForceMode.Impulse);
            collision.collider.gameObject.GetComponent<Rigidbody>().AddRelativeForce(Vector3.forward * diagonalJump, ForceMode.Impulse);
            JumpPadSound.Play(0);
        }

    }
}
