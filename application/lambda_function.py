import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cyberstay-reservations")


def lambda_handler(event, context):


    body = json.loads(event["body"])

    reservation = {
        "reservationId": body["reservationId"],
        "hotel": body["hotel"],
        "room": body["room"],
        "status": "CONFIRMED"
    }

    table.put_item(Item=reservation)

    return {
        "statusCode": 201,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Reservation created successfully",
            "reservation": reservation
        })
    }