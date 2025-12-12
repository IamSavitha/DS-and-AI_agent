require('dotenv').config();
const jwt = require('jsonwebtoken');

const verifyToken = (req, res, next) => {
    // 1. Check for token in the standard Authorization: Bearer header
    const bearerHeader = req.headers['authorization'];

    if (typeof bearerHeader === 'undefined' || !bearerHeader.startsWith('Bearer ')) {
        // 401 Unauthorized - Token missing or badly formed
        return res.status(401).json({ message: "Unauthorized: Bearer token format required." });
    }

    // 2. Extract the token
    const token = bearerHeader.split(' ')[1];
        
    // 3. Verify and decode the token
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
        if (err) {
            // 403 Forbidden - Token is invalid, tampered, or expired
            return res.status(403).json({ 
                message: "Forbidden: Invalid or expired token.",
                errorName: err.name 
            }); 
        }
            
        // 4. Token is valid. Attach the payload (claims) to the request
        req.user = decoded; 
        next();
    });
};

module.exports = verifyToken;