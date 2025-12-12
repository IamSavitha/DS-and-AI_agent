# Short Answer Questions (3 Marks) - Slides 00-05

This file contains short answer questions with answers for lecture slides 00-05.

---

# Slide 00 – Introduction to Distributed Systems

## Short Answer Questions (3 Marks Each)

### Q1. What is a distributed system and what are its key characteristics?

**Answer:**
A distributed system is a collection of independent computers that appear to users as a single coherent system. Key characteristics: (1) **Multiple machines** - components spread across different computers; (2) **Network communication** - machines communicate over a network; (3) **Concurrency** - multiple processes execute simultaneously; (4) **Lack of global clock** - no single time reference; (5) **Independent failures** - components can fail independently. Goals include resource sharing, scalability, and fault tolerance.

### Q2. Explain the difference between monolithic and microservices architecture.

**Answer:**
**Monolithic architecture**: Single application with all components tightly coupled, deployed as one unit. Benefits: simpler development, easier testing. Drawbacks: difficult to scale, single point of failure, hard to update individual components. **Microservices architecture**: Application split into small, independent services. Benefits: independent scaling, fault isolation, technology diversity, independent deployment. Drawbacks: more complex, network latency, distributed system challenges. Microservices are better for large, scalable applications.

### Q3. What is the MERN stack and what does each component do?

**Answer:**
MERN stack is a full-stack JavaScript framework: (1) **MongoDB** - NoSQL document database for data storage; (2) **Express.js** - Web application framework for Node.js, handles routing and middleware; (3) **React** - Frontend library for building user interfaces with components; (4) **Node.js** - JavaScript runtime for server-side execution. Together, they enable full-stack JavaScript development - same language (JavaScript) for frontend and backend, making development more efficient.

### Q4. What are the main challenges in distributed systems?

**Answer:**
Main challenges: (1) **Network latency** - delay in communication between nodes; (2) **Partial failures** - some components fail while others continue; (3) **Concurrency issues** - multiple processes accessing shared resources simultaneously; (4) **Consistency vs Availability** - trade-off between data consistency and system availability (CAP theorem); (5) **Lack of global clock** - difficult to determine event ordering; (6) **Security** - distributed systems are more vulnerable to attacks. These challenges require careful design and trade-offs.

### Q5. Explain the difference between horizontal and vertical scalability.

**Answer:**
**Horizontal scalability (scaling out)**: Adding more machines/nodes to handle increased load. Benefits: can scale almost infinitely, cost-effective (commodity hardware), better fault tolerance. Example: adding more servers to a web application. **Vertical scalability (scaling up)**: Adding more power (CPU, RAM) to existing machines. Benefits: simpler (no code changes), no network overhead. Drawbacks: limited by hardware, expensive, single point of failure. Distributed systems favor horizontal scalability.

### Q6. What is fault tolerance in distributed systems?

**Answer:**
Fault tolerance is the ability of a system to continue operating correctly even when some components fail. Achieved through: (1) **Redundancy** - multiple copies of components; (2) **Replication** - data stored in multiple locations; (3) **Failover** - automatic switching to backup components; (4) **Error detection and recovery** - identifying and handling failures. Benefits: high availability, reliability, graceful degradation. Example: if one server fails, others continue serving requests.

### Q7. Explain the client-server architecture pattern.

**Answer:**
Client-server architecture separates systems into clients (request services) and servers (provide services). **Client**: Makes requests, displays results, user interface. **Server**: Processes requests, manages resources, provides services. Communication: clients send requests over network, servers respond. Benefits: centralized management, security, resource sharing. Examples: web browsers (clients) and web servers, database clients and database servers. This is the foundation of most distributed systems.

### Q8. What is network latency and why is it important in distributed systems?

**Answer:**
Network latency is the delay between sending a request and receiving a response over a network. Measured in milliseconds. Important because: (1) **Performance impact** - high latency slows down applications; (2) **User experience** - affects responsiveness; (3) **Design decisions** - influences architecture choices (synchronous vs asynchronous); (4) **Caching** - often used to reduce latency; (5) **Geographic distribution** - latency increases with distance. Distributed systems must account for latency in design, using techniques like caching, async operations, and data locality.

### Q9. What is eventual consistency and when is it acceptable?

**Answer:**
Eventual consistency means data will become consistent across all nodes eventually, but not immediately. After updates, different nodes may temporarily show different data, but they will converge to the same state. Acceptable when: (1) **High availability** is more important than immediate consistency; (2) **Read-heavy workloads** - most operations are reads; (3) **Geographic distribution** - nodes far apart; (4) **Tolerable staleness** - slightly old data is acceptable. Examples: social media feeds, DNS, CDN content. Trade-off: better availability and performance, but temporary inconsistency.

### Q10. Explain the CAP theorem and its implications.

**Answer:**
CAP theorem states that in a distributed system, you can only guarantee 2 out of 3 properties: (1) **Consistency (C)** - all nodes see same data simultaneously; (2) **Availability (A)** - system remains operational; (3) **Partition Tolerance (P)** - system continues despite network failures. Implications: must choose which to prioritize. **CP system**: Consistency + Partition tolerance (e.g., databases); **AP system**: Availability + Partition tolerance (e.g., web caches); **CA system**: Not possible in truly distributed systems. Design decisions depend on application requirements.

### Q11. What is a message queue and why is it used in distributed systems?

**Answer:**
Message queue is a communication mechanism that enables asynchronous message passing between services. Messages are stored in a queue until processed. Used because: (1) **Decoupling** - services don't need direct connections; (2) **Asynchronous processing** - non-blocking operations; (3) **Reliability** - messages persist if service is down; (4) **Load balancing** - distribute work across multiple workers; (5) **Scalability** - handle traffic spikes. Examples: Kafka, RabbitMQ, Amazon SQS. Enables resilient, scalable distributed architectures.

### Q12. What is the difference between synchronous and asynchronous communication?

**Answer:**
**Synchronous communication**: Sender waits for response before continuing. Blocking operation - client is idle until server responds. Benefits: simpler to understand, immediate feedback. Drawbacks: poor resource utilization, slow if server is busy. **Asynchronous communication**: Sender continues immediately, response handled later (via callback, promise, or message). Non-blocking - client can do other work. Benefits: better resource utilization, handles high load, more responsive. Drawbacks: more complex, harder to debug. Distributed systems often use async for better performance and scalability.

---

# Slide 01 – REST APIs and Node.js

## Short Answer Questions (3 Marks Each)

### Q1. What is REST and what are its key principles?

**Answer:**
REST (Representational State Transfer) is an architectural style for designing networked applications. Key principles: (1) **Stateless** - each request contains all information needed; (2) **Resource-based** - URLs represent resources (nouns), not actions; (3) **HTTP methods** - use standard verbs (GET, POST, PUT, DELETE); (4) **Uniform interface** - consistent way to interact with resources; (5) **Client-server** - separation of concerns; (6) **Cacheable** - responses can be cached; (7) **Layered system** - architecture can have multiple layers. REST enables scalable, maintainable web services.

### Q2. Explain the HTTP methods used in REST APIs and their purposes.

**Answer:**
REST uses standard HTTP methods: (1) **GET** - retrieve data (read-only, idempotent, safe); (2) **POST** - create new resources (not idempotent, sends data in body); (3) **PUT** - update/replace entire resource (idempotent, sends complete resource); (4) **PATCH** - partial update (modify specific fields); (5) **DELETE** - remove resource (idempotent). Each method has semantic meaning: GET for reading, POST for creating, PUT/PATCH for updating, DELETE for removing. Proper use makes APIs intuitive and predictable.

### Q3. What does "stateless" mean in REST and why is it important?

**Answer:**
Stateless means the server doesn't store any client context between requests. Each request contains all information needed to process it (authentication, parameters, etc.). Important because: (1) **Scalability** - any server can handle any request; (2) **Simplicity** - no session management needed; (3) **Reliability** - server failures don't lose state; (4) **Caching** - responses can be cached easily; (5) **Load balancing** - requests can be distributed to any server. Trade-off: client must send all data each time (can use tokens for authentication).

### Q4. What is Node.js and what makes it suitable for backend development?

**Answer:**
Node.js is a JavaScript runtime built on Chrome's V8 engine that allows running JavaScript on the server. Suitable for backend because: (1) **JavaScript everywhere** - same language for frontend and backend; (2) **Non-blocking I/O** - event-driven, handles many concurrent connections efficiently; (3) **Fast** - V8 engine is highly optimized; (4) **NPM ecosystem** - vast library of packages; (5) **Real-time applications** - great for WebSockets, chat apps; (6) **Microservices** - lightweight, fast startup. Ideal for I/O-intensive applications, less suitable for CPU-intensive tasks.

### Q5. Explain the difference between blocking and non-blocking I/O in Node.js.

**Answer:**
**Blocking I/O**: Operations wait until complete before continuing. If reading a file, program stops until file is read. Other operations must wait. **Non-blocking I/O**: Operations start and continue immediately. Program doesn't wait - uses callbacks, promises, or async/await to handle results when ready. Node.js uses non-blocking I/O: (1) **Event loop** - manages async operations; (2) **Single thread** - but handles many operations concurrently; (3) **Efficient** - can handle thousands of connections. Example: `fs.readFile()` is non-blocking - starts reading, continues execution, calls callback when done.

### Q6. What is Express.js and what are its main features?

**Answer:**
Express.js is a minimal, flexible web application framework for Node.js. Main features: (1) **Routing** - define endpoints and handlers; (2) **Middleware** - functions that process requests (authentication, parsing, logging); (3) **Template engines** - render dynamic HTML (EJS, Pug); (4) **Static files** - serve CSS, images, etc.; (5) **Error handling** - centralized error management; (6) **HTTP utilities** - request/response helpers. Simplifies building web servers and APIs. Minimal but extensible - add features via middleware.

### Q7. Explain the request-response cycle in Express.js.

**Answer:**
Request-response cycle: (1) **Client sends HTTP request** - to Express server; (2) **Middleware stack** - request passes through middleware (parsing, authentication, logging); (3) **Route matching** - Express matches URL and HTTP method to route handler; (4) **Route handler executes** - processes request, accesses `req` object (params, body, query); (5) **Response sent** - handler uses `res` object (json(), send(), status()) to send response; (6) **Client receives response**. Middleware can modify request/response or end cycle early. Order matters - middleware executes sequentially.

### Q8. What is middleware in Express.js and how does it work?

**Answer:**
Middleware are functions that execute during the request-response cycle. They have access to `req`, `res`, and `next`. Process: (1) **Receive request** - middleware gets req, res objects; (2) **Process** - can modify req/res, perform operations (parse body, check auth); (3) **Call next()** - passes control to next middleware/route; (4) **Or end cycle** - can send response and stop. Types: application-level (all routes), router-level (specific routes), error-handling. Examples: body-parser (parses JSON), authentication (checks tokens), CORS (handles cross-origin). Enables modular, reusable request processing.

### Q9. What are RESTful URL design principles?

**Answer:**
RESTful URLs should: (1) **Use nouns, not verbs** - `/users` not `/getUsers`; (2) **Use plural nouns** - `/products` not `/product`; (3) **Use hierarchical structure** - `/users/123/posts` for nested resources; (4) **Use HTTP methods for actions** - GET/POST/PUT/DELETE, not `/deleteUser`; (5) **Use query parameters for filtering** - `/users?role=admin`; (6) **Use path parameters for IDs** - `/users/123` not `/users?id=123`; (7) **Keep URLs simple and readable** - `/api/v1/users` not `/api/v1/getAllUsersEndpoint`. Good URLs are self-documenting and intuitive.

### Q10. Explain HTTP status codes and their meanings in REST APIs.

**Answer:**
HTTP status codes indicate request result: **2xx Success**: 200 OK (successful GET/PUT), 201 Created (successful POST), 204 No Content (successful DELETE). **4xx Client Error**: 400 Bad Request (invalid input), 401 Unauthorized (not authenticated), 403 Forbidden (authenticated but not authorized), 404 Not Found (resource doesn't exist), 422 Unprocessable Entity (validation failed). **5xx Server Error**: 500 Internal Server Error (server problem), 503 Service Unavailable. Proper status codes help clients understand results and handle errors appropriately.

### Q11. What is the difference between req.params, req.query, and req.body in Express?

**Answer:**
**req.params**: URL path parameters (e.g., `/users/:id` → `req.params.id`). Defined in route path, required. Example: GET `/users/123` → `req.params.id = "123"`. **req.query**: Query string parameters (e.g., `/users?page=1&limit=10` → `req.query.page = "1"`). Optional, for filtering/sorting. Example: GET `/users?role=admin` → `req.query.role = "admin"`. **req.body**: Request body data (JSON, form data). Requires body-parser middleware. Used in POST/PUT requests. Example: POST `/users` with `{name: "John"}` → `req.body.name = "John"`. Each serves different purposes in REST APIs.

### Q12. What is CORS and why is it needed in REST APIs?

**Answer:**
CORS (Cross-Origin Resource Sharing) is a security mechanism that allows web pages to make requests to different domains. Needed because browsers enforce same-origin policy - by default, JavaScript can only request same domain. When frontend (localhost:3000) calls backend API (localhost:5000), browser blocks it without CORS. Solution: backend sends CORS headers (`Access-Control-Allow-Origin: *`) allowing cross-origin requests. Express uses `cors` middleware to handle this. Important for modern web apps where frontend and backend are separate services.

### Q13. Explain the module system in Node.js (require and module.exports).

**Answer:**
Node.js uses CommonJS module system. **module.exports**: Exports values/functions from a module. Example: `module.exports = { add, subtract }` or `module.exports = myFunction`. **require()**: Imports modules. Example: `const math = require('./math.js')` or `const express = require('express')`. Modules are cached - first require loads and caches, subsequent requires return cached version. Enables: code organization, reusability, dependency management. Each file is a module with its own scope. This is how Node.js organizes and shares code.

### Q14. What is package.json and what information does it contain?

**Answer:**
package.json is a manifest file for Node.js projects. Contains: (1) **Project metadata** - name, version, description; (2) **Dependencies** - packages needed in production (`dependencies`) and development (`devDependencies`); (3) **Scripts** - commands like `npm start`, `npm test`; (4) **Entry point** - main file (`main`); (5) **Engine requirements** - Node.js version; (6) **Repository info** - GitHub URL, etc. Used by npm to install dependencies, run scripts, and manage project. Essential for sharing and deploying Node.js projects.

### Q15. What is the difference between dependencies and devDependencies in package.json?

**Answer:**
**dependencies**: Packages needed in production (when app runs). Examples: express, mongoose, axios. Installed with `npm install <package>`. Included when deploying. **devDependencies**: Packages needed only during development. Examples: nodemon, jest, eslint. Installed with `npm install <package> --save-dev`. Not included in production builds. Separation benefits: smaller production builds, clearer dependencies, faster installs. Use devDependencies for testing, building, linting tools that aren't needed at runtime.

---

# Slide 02 – Session Management and Prompts

## Short Answer Questions (3 Marks Each)

### Q1. What is session-based authentication and how does it work?

**Answer:**
Session-based authentication maintains user state on the server. Process: (1) **User logs in** - submits credentials; (2) **Server validates** - checks username/password; (3) **Server creates session** - stores session data server-side with unique session ID; (4) **Server sends cookie** - session ID sent to client in Set-Cookie header; (5) **Client includes cookie** - sends session ID in subsequent requests; (6) **Server validates** - looks up session by ID, retrieves user data. Session data stored server-side (memory, database, Redis), more secure than client-side storage.

### Q2. Explain the difference between session-based and token-based authentication.

**Answer:**
**Session-based**: Server stores session data, sends session ID cookie. Client sends cookie with each request. Server looks up session. **Stateful** - server maintains state. **Token-based (JWT)**: Server creates token with user data, sends to client. Client sends token in header. Server validates token (no lookup needed). **Stateless** - all data in token. Comparison: Sessions require server storage, tokens don't. Sessions can be revoked immediately, tokens can't (until expiration). Sessions work better for single-server, tokens for distributed systems. Tokens are more scalable.

### Q3. What is express-session middleware and how is it configured?

**Answer:**
express-session is middleware that manages sessions in Express.js. Configuration options: (1) **secret** - used to sign session cookie (prevents tampering); (2) **resave** - whether to save session even if unmodified (usually false); (3) **saveUninitialized** - whether to create session before storing data (usually false for security); (4) **cookie** - cookie settings (secure: HTTPS only, httpOnly: no JavaScript access, maxAge: expiration time); (5) **store** - where to store sessions (memory default, or Redis/database). Example: `app.use(session({ secret: 'key', resave: false, saveUninitialized: false }))`. Handles session creation, storage, and cookie management automatically.

### Q4. What is password hashing and why is bcrypt used?

**Answer:**
Password hashing converts plain text passwords into irreversible scrambled strings using one-way functions. **Why hash**: Never store plain text passwords - if database is compromised, attackers can't see actual passwords. **bcrypt**: Specifically designed for passwords. Features: (1) **Automatic salting** - adds random salt to each password; (2) **Adaptive hashing** - can increase cost factor (rounds) as computers get faster; (3) **Slow by design** - makes brute-force attacks impractical; (4) **Proven security** - widely used and tested. Format: `$2b$10$salt22charactershashedpassword31characters`. Verification: bcrypt.compare() automatically extracts salt and compares.

### Q5. Explain how session cookies work and their security properties.

**Answer:**
Session cookies store session ID on client. Process: (1) **Server creates session** - generates unique session ID; (2) **Server sends cookie** - `Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Strict`; (3) **Browser stores cookie** - automatically stores and sends with requests; (4) **Client sends cookie** - browser includes in Cookie header automatically. Security properties: **HttpOnly** - prevents JavaScript access (XSS protection); **Secure** - only sent over HTTPS; **SameSite** - prevents CSRF attacks; **MaxAge** - expiration time. Session ID should be random, unpredictable, and signed to prevent tampering.

### Q6. What is prompt engineering and why is it important for LLMs?

**Answer:**
Prompt engineering is the practice of designing effective inputs (prompts) to get desired outputs from LLMs. Important because: (1) **Output quality** - well-crafted prompts produce better results; (2) **Consistency** - structured prompts ensure consistent behavior; (3) **Efficiency** - good prompts reduce need for multiple attempts; (4) **Control** - guides LLM toward specific tasks; (5) **Cost** - better prompts = fewer API calls. Techniques: clear instructions, examples (few-shot), role definition, output format specification, chain-of-thought reasoning. Critical skill for building LLM applications.

### Q7. What are the key components of an effective prompt?

**Answer:**
Effective prompts include: (1) **Role definition** - "You are an expert programmer" sets context; (2) **Clear task** - specific, unambiguous instructions; (3) **Context** - relevant background information; (4) **Examples** - few-shot learning with input-output pairs; (5) **Output format** - specify desired structure (JSON, list, etc.); (6) **Constraints** - limitations and requirements; (7) **Chain-of-thought** - "think step by step" for complex reasoning. Well-structured prompts guide LLM behavior and improve accuracy. Example: "You are a helpful assistant. Format responses as JSON. Here's an example: {...}"

### Q8. Explain the difference between system prompts and user prompts.

**Answer:**
**System prompt**: Defines the LLM's role, behavior, and constraints. Sets overall context and personality. Usually set once per conversation. Example: "You are a helpful coding assistant. Always explain your reasoning." **User prompt**: The actual task or question from the user. Changes with each interaction. Example: "Write a function to sort an array." In API calls: system prompt in `system` message, user prompt in `user` message. System prompt establishes "who" the LLM is, user prompt is "what" to do. Both are important for controlling LLM behavior.

### Q9. What is few-shot learning in prompt engineering?

**Answer:**
Few-shot learning provides examples in the prompt to guide LLM behavior. Instead of just instructions, include input-output examples. Process: (1) **Show examples** - demonstrate desired behavior with 2-5 examples; (2) **LLM learns pattern** - infers pattern from examples; (3) **Apply to new input** - LLM follows pattern for new requests. Benefits: (1) **Better accuracy** - examples clarify expectations; (2) **Format consistency** - shows exact output format; (3) **Complex tasks** - easier than describing in words. Example: "Translate: 'Hello' → 'Hola', 'Goodbye' → 'Adiós'. Now translate: 'Thank you'"

### Q10. What is chain-of-thought prompting and how does it work?

**Answer:**
Chain-of-thought prompting asks LLM to show its reasoning process step-by-step. Instead of direct answer, LLM explains thinking. Process: (1) **Request reasoning** - "think step by step" or "show your work"; (2) **LLM breaks down** - decomposes problem into steps; (3) **Shows intermediate** - explains each step; (4) **Reaches conclusion** - final answer based on reasoning. Benefits: (1) **Better accuracy** - reasoning improves correctness; (2) **Transparency** - see how answer was derived; (3) **Error detection** - can spot mistakes in reasoning; (4) **Learning** - helps understand LLM thinking. Useful for complex problems requiring multi-step reasoning.

### Q11. What is temperature in LLM prompts and how does it affect output?

**Answer:**
Temperature (0-2) controls randomness/creativity in LLM responses. **Low temperature (0-0.3)**: Deterministic, consistent, focused. Same input → similar output. Good for: factual answers, code generation, structured data. **High temperature (0.7-2)**: Creative, varied, unpredictable. Same input → different outputs. Good for: creative writing, brainstorming, diverse ideas. **Default (~0.7)**: Balanced. Too high = incoherent, too low = repetitive. Temperature is a hyperparameter set when calling LLM API. Choose based on task requirements - consistency vs creativity.

### Q12. Explain session storage options and their trade-offs.

**Answer:**
Session storage options: (1) **Memory store (default)** - stores in server RAM. Fast, simple, but lost on restart, not shared across servers. Good for development. (2) **Database store** - stores in database (MongoDB, PostgreSQL). Persistent, shared across servers, but slower. Good for production. (3) **Redis store** - in-memory database. Fast, persistent, shared, scalable. Best for production. Trade-offs: Memory = fast but not persistent; Database = persistent but slower; Redis = fast and persistent but requires Redis server. Choose based on requirements: single server vs distributed, persistence needs, performance requirements.

### Q13. What is session hijacking and how can it be prevented?

**Answer:**
Session hijacking is stealing someone's session ID to impersonate them. Attackers get session ID (from network sniffing, XSS, etc.) and use it to access account. Prevention: (1) **HTTPS only** - encrypts traffic, prevents sniffing; (2) **HttpOnly cookies** - prevents JavaScript access (XSS protection); (3) **Secure cookies** - only sent over HTTPS; (4) **Session timeout** - expire sessions after inactivity; (5) **Regenerate session ID** - after login to prevent fixation; (6) **IP validation** - check if request comes from same IP (can break with mobile); (7) **User agent validation** - check browser fingerprint. Multiple layers provide defense.

### Q14. What is the difference between session and cookie expiration?

**Answer:**
**Session expiration**: When server-side session data expires/is deleted. After expiration, session ID is invalid even if cookie exists. Set via session store configuration. **Cookie expiration (maxAge)**: When browser deletes the cookie. After expiration, browser stops sending cookie. Set via cookie.maxAge. Both should be coordinated: (1) **Cookie expires first** - browser stops sending, but session still valid (wasteful); (2) **Session expires first** - cookie sent but session invalid (better security); (3) **Both expire together** - ideal. Typically: session timeout = 30 minutes, cookie maxAge = same or slightly longer. Prevents stale sessions.

---

# Slide 03 – React.js and Model Context Protocol (MCP)

## Short Answer Questions (3 Marks Each)

### Q1. What is React and what are its key features?

**Answer:**
React is a JavaScript library for building user interfaces, especially interactive web applications. Key features: (1) **Component-based** - build UI from reusable components; (2) **Virtual DOM** - efficient updates by comparing virtual representations; (3) **Declarative** - describe what UI should look like, React handles how; (4) **Unidirectional data flow** - data flows down via props, events flow up; (5) **JSX** - JavaScript syntax extension for writing HTML-like code; (6) **Hooks** - functions for state and side effects (useState, useEffect); (7) **React ecosystem** - large community, many libraries. Enables building complex, interactive UIs efficiently.

### Q2. Explain the difference between props and state in React.

**Answer:**
**Props (properties)**: Data passed from parent to child component. Immutable - child cannot modify props. Used for: configuration, initial values, data from parent. Example: `<User name="John" age={25} />` - name and age are props. **State**: Internal data managed by component. Mutable - component can update using setState/useState. Used for: user input, UI state, dynamic data. Example: `const [count, setCount] = useState(0)`. Key difference: Props flow down (parent → child), state is local to component. Props are read-only, state can be updated. Both trigger re-renders when changed.

### Q3. What are React hooks and explain useState and useEffect.

**Answer:**
React hooks are functions that let functional components use state and lifecycle features. **useState**: Manages component state. Returns [value, setter]. Example: `const [count, setCount] = useState(0)` - count is value, setCount updates it. Calling setCount triggers re-render. **useEffect**: Handles side effects (API calls, subscriptions, DOM manipulation). Runs after render. Example: `useEffect(() => { fetchData() }, [dependencies])` - runs when dependencies change. Empty array [] = run once (mount). No array = run every render. Dependencies = run when they change. Hooks enable functional components to have state and effects like class components.

### Q4. What is JSX and how does it differ from HTML?

**Answer:**
JSX (JavaScript XML) is a syntax extension that lets you write HTML-like code in JavaScript. Differences from HTML: (1) **Must return single element** - wrap multiple elements in fragment `<>` or div; (2) **Use className** - not `class` (class is reserved in JS); (3) **Self-closing tags** - `<img />` not `<img>`; (4) **JavaScript expressions** - use `{}` for variables/expressions: `<h1>{name}</h1>`; (5) **CamelCase attributes** - `onClick` not `onclick`; (6) **Compiled to JavaScript** - Babel converts JSX to React.createElement() calls. JSX makes React code more readable and intuitive than pure JavaScript function calls.

### Q5. Explain the React component lifecycle and useEffect equivalents.

**Answer:**
Component lifecycle: (1) **Mount** - component created and added to DOM; (2) **Update** - component re-renders when props/state change; (3) **Unmount** - component removed from DOM. **useEffect equivalents**: (1) **componentDidMount** - `useEffect(() => {...}, [])` - empty dependency array runs once on mount; (2) **componentDidUpdate** - `useEffect(() => {...}, [deps])` - runs when dependencies change; (3) **componentWillUnmount** - `useEffect(() => { return () => {...} }, [])` - cleanup function runs on unmount. useEffect combines multiple lifecycle methods into one hook. Dependencies control when effect runs.

### Q6. What is the virtual DOM and how does it improve performance?

**Answer:**
Virtual DOM is a JavaScript representation of the real DOM. React creates virtual DOM tree, compares with previous version (diffing), and updates only changed parts (reconciliation). Process: (1) **State change** - component state updates; (2) **Virtual DOM created** - React creates new virtual DOM tree; (3) **Diffing** - compares new tree with previous; (4) **Minimal updates** - calculates minimum DOM changes needed; (5) **Batch updates** - applies changes efficiently. Benefits: (1) **Performance** - avoids expensive full DOM updates; (2) **Efficiency** - only updates what changed; (3) **Predictability** - easier to reason about updates. Virtual DOM is faster than direct DOM manipulation for complex UIs.

### Q7. What is Model Context Protocol (MCP) and what problem does it solve?

**Answer:**
MCP (Model Context Protocol) is a standardized protocol that enables AI assistants to discover, describe, and invoke external tools and services. Solves: (1) **Limited capabilities** - LLMs can only generate text, can't perform actions; (2) **Tool integration** - provides standard way to connect LLMs with external services; (3) **Extensibility** - allows adding new capabilities without modifying LLM; (4) **Interoperability** - standard protocol works across different AI clients and servers. Enables LLMs to: search web, query databases, call APIs, access file systems, perform calculations. Extends LLM capabilities beyond text generation to real-world actions.

### Q8. Explain the MCP architecture and how it works.

**Answer:**
MCP architecture: (1) **AI Client** (Claude, GPT) - the LLM that needs tools; (2) **MCP Server** - provides tools and services; (3) **JSON-RPC communication** - standard protocol for requests/responses; (4) **Tool discovery** - client asks server what tools are available; (5) **Tool schema** - server describes tool parameters and return types; (6) **Tool invocation** - client calls tool with parameters; (7) **External services** - tools connect to APIs, databases, file systems. Flow: Client discovers tools → Gets schemas → Calls tools → Receives results → Uses in reasoning. Enables LLMs to interact with external systems safely and consistently.

### Q9. What is an MCP server and what does it provide?

**Answer:**
MCP server is an application that implements the MCP protocol, providing tools that AI assistants can call. Provides: (1) **Tool definitions** - describes available tools (name, parameters, return types); (2) **Tool implementations** - actual functions that perform actions; (3) **Tool schemas** - JSON schemas describing inputs/outputs; (4) **Security** - validates inputs, restricts access, handles errors; (5) **Integration** - connects to external services (APIs, databases). Examples: Recipe server (searches recipes), Database server (queries database), File server (reads files). MCP servers extend LLM capabilities by providing domain-specific tools.

### Q10. How do MCP tools extend LLM capabilities?

**Answer:**
MCP tools extend LLMs by providing actions beyond text generation. Process: (1) **LLM needs information** - user asks question requiring external data; (2) **LLM discovers tools** - queries MCP server for available tools; (3) **LLM selects tool** - chooses appropriate tool based on task; (4) **LLM calls tool** - invokes tool with parameters; (5) **Tool executes** - performs action (API call, database query, etc.); (6) **Tool returns result** - provides data to LLM; (7) **LLM uses result** - incorporates into response. Enables: web search, calculations, database queries, file operations, API calls. LLMs become agents that can act, not just generate text.

### Q11. What is the difference between MCP and direct API integration?

**Answer:**
**Direct API integration**: LLM application directly calls APIs. Tightly coupled - code must be updated for each API. No standardization - different APIs have different formats. **MCP**: Standardized protocol for tool integration. Benefits: (1) **Standardization** - consistent interface across tools; (2) **Discoverability** - LLM can discover available tools dynamically; (3) **Modularity** - tools are separate services; (4) **Reusability** - same MCP server works with different LLMs; (5) **Security** - centralized access control; (6) **Schema validation** - automatic input/output validation. MCP provides abstraction layer, making tool integration easier and more maintainable.

### Q12. Explain React Router and client-side routing.

**Answer:**
React Router enables client-side routing - navigation without page reloads. Process: (1) **Define routes** - map URLs to components: `<Route path="/users" element={<Users />} />`; (2) **Router component** - wraps app: `<BrowserRouter>`; (3) **Navigation** - use `<Link>` or `useNavigate()` hook; (4) **URL changes** - browser URL updates, but no page reload; (5) **Component renders** - React renders matching component. Benefits: (1) **Faster** - no full page reload; (2) **Smooth UX** - instant navigation; (3) **State preservation** - React state maintained; (4) **SPA** - Single Page Application experience. Enables building multi-page apps that feel like native applications.

### Q13. What are controlled and uncontrolled components in React?

**Answer:**
**Controlled component**: Input value controlled by React state. Value comes from state, onChange updates state. Example: `<input value={name} onChange={(e) => setName(e.target.value)} />`. React controls the input. **Uncontrolled component**: Input manages its own state internally. Use refs to access value. Example: `<input ref={inputRef} />` then `inputRef.current.value`. React doesn't control the input. Controlled is preferred: (1) **Single source of truth** - state in React; (2) **Validation** - can validate on change; (3) **Form handling** - easier to manage forms. Uncontrolled used for: file inputs, third-party libraries, performance-critical cases.

### Q14. What is React's key prop and why is it important?

**Answer:**
The `key` prop helps React identify which items changed, were added, or removed in lists. When rendering lists: `{items.map(item => <Item key={item.id} data={item} />)}`. Important because: (1) **Efficient updates** - React knows which items changed; (2) **Prevents bugs** - correct component reuse; (3) **State preservation** - maintains component state correctly; (4) **Performance** - avoids unnecessary re-renders. Keys should be: (1) **Unique** - each item has unique key; (2) **Stable** - same item has same key across renders; (3) **Not index** - avoid using array index if items can reorder. Without keys, React may incorrectly reuse components, causing bugs.

---

# Slide 04 – Redux, LLM Integration, and FastAPI

## Short Answer Questions (3 Marks Each)

### Q1. What is Redux and what problem does it solve?

**Answer:**
Redux is a predictable state container for JavaScript applications. Solves: (1) **Prop drilling** - passing props through many components; (2) **Global state management** - need to share state across components; (3) **State synchronization** - keeping state consistent; (4) **Complex state updates** - managing state changes predictably. Provides: (1) **Single source of truth** - all state in one store; (2) **Predictable updates** - state changes via actions/reducers; (3) **Time-travel debugging** - Redux DevTools; (4) **Testability** - pure functions easy to test. Better than local state for: large apps, complex state, shared data across many components.

### Q2. Explain the Redux data flow.

**Answer:**
Redux data flow: (1) **Component dispatches action** - `dispatch({ type: 'INCREMENT' })`; (2) **Action sent to reducer** - Redux calls reducer with current state and action; (3) **Reducer returns new state** - pure function: `(state, action) => newState`; (4) **Store updates** - Redux updates store with new state; (5) **Components re-render** - components subscribed to store (via useSelector) automatically re-render with new state. Unidirectional flow: Action → Reducer → Store → Component. This makes state changes predictable and traceable. All state changes go through this flow.

### Q3. What is a Redux reducer and why must it be pure?

**Answer:**
A reducer is a pure function that takes current state and action, returns new state: `(state, action) => newState`. Must be pure because: (1) **Predictability** - same input always produces same output; (2) **Testability** - easy to test pure functions; (3) **Time-travel debugging** - Redux DevTools can replay actions; (4) **No side effects** - no API calls, mutations, or random values. Rules: (1) **Never mutate state** - return new state object; (2) **No side effects** - no async operations, no API calls; (3) **Deterministic** - same state + action = same result. Side effects go in middleware or action creators, not reducers.

### Q4. What are Redux actions and action creators?

**Answer:**
**Actions**: Plain objects describing what happened. Must have `type` property. Can have `payload` for data. Example: `{ type: 'ADD_TODO', payload: { text: 'Learn Redux' } }`. **Action creators**: Functions that return actions. Provide consistency and allow parameters. Example: `const addTodo = (text) => ({ type: 'ADD_TODO', payload: { text } })`. Benefits: (1) **Centralized** - all actions in one place; (2) **Reusable** - can call with different parameters; (3) **Testable** - easy to test action creators; (4) **Type safety** - can add TypeScript types. Dispatch via: `dispatch(addTodo('Learn Redux'))`. Actions describe events, action creators create them.

### Q5. How do you connect React components to Redux store?

**Answer:**
Connect React to Redux: (1) **Wrap app with Provider** - `<Provider store={store}>` makes store available to all components; (2) **Use useSelector hook** - read state: `const count = useSelector(state => state.counter)`; (3) **Use useDispatch hook** - dispatch actions: `const dispatch = useDispatch(); dispatch(increment())`. Process: Provider makes store available → useSelector subscribes to state → useDispatch gets dispatch function → Components can read state and dispatch actions. Components re-render when selected state changes. This is the modern React-Redux approach (hooks), replacing older connect() HOC.

### Q6. What is FastAPI and what are its main advantages?

**Answer:**
FastAPI is a modern Python web framework for building APIs. Advantages: (1) **Automatic API documentation** - generates OpenAPI/Swagger docs automatically; (2) **Type validation** - uses Pydantic for automatic request/response validation; (3) **Async support** - built-in async/await for high performance; (4) **Type hints** - Python type hints for better IDE support; (5) **Fast** - built on Starlette, comparable to Node.js; (6) **Easy to use** - simple syntax, great developer experience. Example: `@app.get("/users/{id}") async def get_user(id: int): return {"id": id}`. Automatic validation, documentation, and serialization.

### Q7. Explain Pydantic models in FastAPI.

**Answer:**
Pydantic models define data structures with validation using Python type hints. Example: `class User(BaseModel): name: str; age: int; email: EmailStr`. FastAPI uses Pydantic for: (1) **Request validation** - automatically validates request body against model; (2) **Response serialization** - converts Python objects to JSON; (3) **Error handling** - returns 422 if validation fails; (4) **OpenAPI schema** - generates API documentation from models. Benefits: (1) **Type safety** - catch errors at development time; (2) **Automatic validation** - no manual checks needed; (3) **Documentation** - models appear in Swagger docs. Pydantic ensures data integrity automatically.

### Q8. What is dependency injection in FastAPI?

**Answer:**
Dependency injection shares common functionality across routes. Example: `@app.get("/users") async def get_users(db: Session = Depends(get_db)): ...`. Process: (1) **Define dependency** - function that provides shared resource (DB session, auth, config); (2) **Use Depends()** - FastAPI calls dependency function; (3) **Inject into route** - dependency result available as parameter. Benefits: (1) **Reusability** - share logic across routes; (2) **Testability** - can mock dependencies; (3) **Clean code** - separation of concerns; (4) **Automatic handling** - FastAPI manages dependency lifecycle. Common uses: database sessions, authentication, configuration, shared services.

### Q9. How do you integrate LLMs (like OpenAI) with FastAPI?

**Answer:**
Integrate LLMs: (1) **Install library** - `pip install openai`; (2) **Set API key** - environment variable `OPENAI_API_KEY`; (3) **Create endpoint** - FastAPI route; (4) **Use async/await** - LLM calls are async; (5) **Handle responses** - process LLM output. Example: `@app.post("/chat") async def chat(message: str): response = await openai.ChatCompletion.acreate(model="gpt-3.5-turbo", messages=[...]); return response.choices[0].message.content`. Use dependency injection for API client, handle errors, set rate limits. FastAPI's async support makes it ideal for LLM integration.

### Q10. What is LangChain and how does it help with LLM applications?

**Answer:**
LangChain is a framework for building applications with LLMs. Helps by: (1) **Abstraction** - simplifies LLM interactions; (2) **Chains** - combines multiple LLM calls sequentially; (3) **Agents** - enables LLMs to use tools; (4) **Memory** - maintains conversation history; (5) **Prompt templates** - reusable prompt structures; (6) **Output parsers** - structured output handling. Example: Chain that searches web → processes results → generates summary. LangChain provides building blocks for complex LLM workflows, making it easier to build production LLM applications than raw API calls.

### Q11. Explain temperature in LLM API calls and its effect.

**Answer:**
Temperature (0-2) controls randomness in LLM responses. **Low (0-0.3)**: Deterministic, consistent, factual. Same prompt → similar output. Use for: code generation, factual answers, structured data. **High (0.7-2)**: Creative, varied, unpredictable. Same prompt → different outputs. Use for: creative writing, brainstorming, diverse ideas. **Default (~0.7)**: Balanced. Too high = incoherent, too low = repetitive. Set in API call: `temperature=0.7`. Choose based on task: need consistency → low, need creativity → high. Temperature is a hyperparameter that significantly affects output quality and style.

### Q12. What is the difference between Redux store and React Context?

**Answer:**
**Redux**: External library, predictable state updates via reducers, DevTools support, middleware support, better for complex state. Requires: store setup, actions, reducers, Provider, hooks. **React Context**: Built into React, simpler setup, good for simple state, no built-in DevTools, can cause performance issues with frequent updates. Requires: createContext, Provider, useContext. **When to use**: Redux for large apps with complex state, Context for simple shared state. Redux provides more features (time-travel, middleware, DevTools) but more setup. Context is simpler but less powerful.

---

# Slide 05 – NoSQL, MongoDB, and Memory Management

## Short Answer Questions (3 Marks Each)

### Q1. What is NoSQL and how does it differ from SQL databases?

**Answer:**
NoSQL (Not Only SQL) are non-relational databases with flexible schemas. Differences: **SQL**: Fixed schemas (tables with columns), ACID transactions, relational (joins), structured queries. **NoSQL**: Flexible schemas (can add fields), eventual consistency, document/key-value/column/graph models, simpler queries. Use NoSQL for: (1) **Flexible data** - changing schemas, unstructured data; (2) **Horizontal scaling** - distributed systems; (3) **Rapid development** - no migrations needed; (4) **Large scale** - big data, high throughput. Use SQL for: complex relationships, ACID requirements, structured data. NoSQL trades consistency and relationships for flexibility and scalability.

### Q2. What is MongoDB and what type of database is it?

**Answer:**
MongoDB is a document-based NoSQL database. Stores data as documents (BSON - Binary JSON) in collections. Documents are like JSON objects with nested data. Type: **Document database** - stores documents (not tables/rows). Structure: Database → Collections → Documents. Features: (1) **Flexible schema** - documents can have different fields; (2) **Embedded documents** - nested objects/arrays; (3) **Indexing** - fast queries; (4) **Horizontal scaling** - sharding across servers; (5) **Rich queries** - powerful query language. Example document: `{ name: "John", age: 30, address: { city: "NYC" } }`. Good for: content management, user profiles, real-time analytics.

### Q3. Explain the difference between embedding and referencing in MongoDB.

**Answer:**
**Embedding**: Store related data in same document. Example: User document contains address object. Benefits: (1) **Fast reads** - single query gets all data; (2) **Atomic updates** - update everything together; (3) **No joins** - data already together. Use when: one-to-few relationship, data accessed together, data doesn't change independently. **Referencing**: Store IDs, separate documents. Example: User document has `addressId`, Address in separate collection. Benefits: (1) **Flexibility** - update independently; (2) **Avoid duplication** - share data; (3) **Size limits** - MongoDB has 16MB document limit. Use when: one-to-many/many-to-many, data accessed independently, large documents. Trade-off: Embedding = faster reads, referencing = more flexible updates.

### Q4. What is Mongoose and how does it help with MongoDB?

**Answer:**
Mongoose is an ODM (Object Document Mapper) for MongoDB in Node.js. Helps by: (1) **Schema definition** - defines document structure with validation; (2) **Models** - provides methods to interact with collections (find, save, update); (3) **Validation** - automatic data validation; (4) **Middleware** - pre/post hooks (before save, after find); (5) **Type casting** - converts types automatically; (6) **Query building** - easier query syntax. Example: `const User = mongoose.model('User', userSchema); await User.find({ age: { $gte: 18 } })`. Mongoose adds structure and validation to MongoDB while keeping flexibility. Makes MongoDB easier to use with type safety and validation.

### Q5. What is the MongoDB aggregation pipeline?

**Answer:**
Aggregation pipeline processes documents through multiple stages sequentially. Each stage transforms documents. Stages: (1) **$match** - filter documents (like WHERE); (2) **$group** - aggregate data (sum, avg, count); (3) **$sort** - sort results; (4) **$project** - select/rename fields; (5) **$limit** - limit results. Example: `[{ $match: { status: 'completed' }}, { $group: { _id: '$customerId', total: { $sum: '$amount' }}}, { $sort: { total: -1 }}]`. Powerful for: complex queries, data analysis, transformations. Like SQL GROUP BY but more flexible. Pipeline processes documents stage by stage, each stage receives output from previous.

### Q6. What is indexing in MongoDB and why is it important?

**Answer:**
Indexing creates data structures that improve query performance. Without index: MongoDB scans entire collection (slow). With index: Direct lookup (fast). Process: (1) **Create index** - on frequently queried fields; (2) **MongoDB maintains** - updates index when data changes; (3) **Queries use index** - MongoDB uses index for fast lookups. Trade-off: Faster reads, slower writes (indexes must be updated). Example: `db.users.createIndex({ email: 1 })` - index on email field. MongoDB automatically indexes `_id`. Use indexes on: frequently queried fields, fields used in sorting, fields in WHERE clauses. Critical for performance in large collections.

### Q7. Explain memory management in Node.js applications.

**Answer:**
Node.js memory management: (1) **Heap memory** - where objects are stored; (2) **Garbage collection** - automatically frees unused memory; (3) **Memory leaks** - memory allocated but never freed. Common causes: (1) **Event listeners** - not removed; (2) **Closures** - holding large references; (3) **Global variables** - accumulating data; (4) **Timers** - not cleared. Prevention: (1) Remove listeners; (2) Avoid global state; (3) Clear intervals/timeouts; (4) Use streams for large data; (5) Monitor memory usage. Node.js uses V8's garbage collector. Memory leaks cause: increasing memory usage, eventual crashes, poor performance. Important to manage memory in long-running Node.js applications.

### Q8. What is connection pooling and why is it important?

**Answer:**
Connection pooling reuses database connections instead of creating new ones for each request. Process: (1) **Create pool** - pre-create connections; (2) **Reuse connections** - requests borrow from pool; (3) **Return to pool** - after use, connection returned; (4) **Limit connections** - pool has max size. Important because: (1) **Performance** - creating connections is slow; (2) **Resource efficiency** - reuse existing connections; (3) **Scalability** - limits connections (prevents overload); (4) **Cost** - databases have connection limits. Without pooling: each request creates/tears down connection (slow, resource-intensive). With pooling: fast, efficient, scalable. Essential for production applications.

### Q9. What are Mongoose middleware/hooks and provide examples?

**Answer:**
Mongoose middleware (hooks) execute functions before/after operations. Types: **pre hooks** - run before operation (save, find, remove); **post hooks** - run after operation. Examples: (1) **Pre-save hook** - hash password before saving: `schema.pre('save', async function() { this.password = await bcrypt.hash(this.password, 10); })`; (2) **Post-find hook** - log after finding: `schema.post('find', function(docs) { console.log('Found', docs.length); })`. Use for: validation, transformations, logging, side effects. Middleware runs automatically when operations occur. Enables: password hashing, timestamps, logging, data transformations. Powerful feature for adding behavior to models.

### Q10. Explain the difference between MongoDB queries and SQL queries.

**Answer:**
**MongoDB**: Method-based queries, uses operators ($gt, $in, $or), embedded documents, method chaining. Example: `db.users.find({ age: { $gte: 18 }, city: "NYC" })`. **SQL**: Declarative language, uses keywords (SELECT, WHERE, JOIN), normalized tables, joins for relationships. Example: `SELECT * FROM users WHERE age >= 18 AND city = 'NYC'`. Differences: (1) **Syntax** - MongoDB methods vs SQL keywords; (2) **Relationships** - MongoDB embedding vs SQL joins; (3) **Flexibility** - MongoDB flexible schema vs SQL fixed schema; (4) **Nested data** - MongoDB handles easily, SQL requires joins. MongoDB: more flexible for nested data, JSON-like. SQL: better for complex joins, standardized.

### Q11. What is garbage collection in Node.js and how does it work?

**Answer:**
Garbage collection automatically frees memory of unused objects. Node.js uses V8's garbage collector. Process: (1) **Mark** - identifies objects still in use (reachable from roots); (2) **Sweep** - removes unreachable objects; (3) **Compact** - defragments memory. Types: (1) **Scavenge** - fast, for new objects; (2) **Mark-sweep** - for old objects; (3) **Incremental** - doesn't pause execution. Works automatically - developers don't manage memory manually. However, memory leaks occur when objects remain reachable but unused (event listeners, closures, global variables). Garbage collection can't free memory that's still referenced. Important to write code that allows GC to work effectively.

### Q12. What are common causes of memory leaks in Node.js?

**Answer:**
Common causes: (1) **Event listeners** - added but never removed, keeping objects in memory; (2) **Closures** - holding references to large objects; (3) **Global variables** - accumulating data over time; (4) **Timers** - setInterval/setTimeout not cleared; (5) **Caches without limits** - growing indefinitely; (6) **Circular references** - objects referencing each other. Prevention: (1) Remove event listeners when done; (2) Avoid global state; (3) Clear intervals/timeouts; (4) Use WeakMap/WeakSet for weak references; (5) Limit cache sizes; (6) Monitor memory usage. Memory leaks cause: increasing memory usage, eventual crashes, poor performance. Critical to identify and fix in production applications.

---

**End of Questions**

