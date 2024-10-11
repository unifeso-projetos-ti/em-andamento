using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FisicaBola : MonoBehaviour
{
    // Start is called before the first frame update
   
    void OnCollisionEnter (Collision collisionInfo)
    {
        if (collisionInfo.collider.name == "Obstacle")
        {
            Debug.Log("fsygdfaksjd");
        }
    }
}
