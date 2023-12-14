# Use the official Node.js image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the React app files to the container
COPY . .

# Build the React app for production
RUN npm run build

# Set the command to serve the React app using a simple HTTP server (for production build)
# Change the serve command based on your setup (e.g., serve -s build)
CMD ["npx", "serve", "-s", "build"]
