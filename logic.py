from database import get_connection

def addCard(cardName, cardNum, quantity, location):
    conn = get_connection()
    cur = conn.cursor()
    
    cardName.strip()
    cardNum.strip()
    
    if cardName == "" or cardNum == "":
        return False
    
    cur.execute("""
                INSERT INTO cards (cardN, cardID, quantity, location)
                VALUES (?, ?, ?, ?)
                """, (cardName, cardNum, quantity, location))
    
    conn.commit()
    conn.close()

def deleteCard(cardName, cardNum):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
                DELETE FROM cards
                WHERE cardN = ?
                AND cardID = ?
                """, (cardName, cardNum))
    
    conn.commit()
    conn.close()

def searchCard(cardName, cardNum):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
                SELECT cardN, cardID, quantity, location FROM cards WHERE cardN LIKE? AND cardID LIKE ?
                """, ("%" + cardName + "%", "%" + cardNum + "%"))
    
    result = cur.fetchall()
    conn.close()
    
    return result

def getAllCards():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
                SELECT cardN, cardID, quantity, location
                FROM cards
                """)
    
    result = cur.fetchall()
    conn.close()
    
    return result