# Use official Node.js image as base image
FROM node:20

# Set working directory in the container
WORKDIR /frontend

# Copy package.json and package-lock.json to work directory
COPY ./package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port 5173 to the outside world
EXPOSE 5173

# Command to run the application
CMD ["npm", "run", "dev"]