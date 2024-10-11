using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerKick : MonoBehaviour
{
    public float power;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnControllerColliderHit(ControllerColliderHit hit){
        if(hit.collider.CompareTag("bola")){
            Rigidbody rb = hit.collider.GetComponent<Rigidbody>();

            if(rb != null){
                Vector3 direction = hit.gameObject.transform.position - this.transform.position;
                direction.y = 0;
                direction.Normalize();
                rb.AddForceAtPosition(direction * power, transform.position, ForceMode.Impulse);
            }
        }
    }
    
}
