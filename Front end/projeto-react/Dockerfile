# Use an official Node runtime as the base image
FROM node:20-alpine

# Set the working directory in the container
WORKDIR /app
# Copy the rest of the application code
COPY . /app/
# Install dependencies
RUN npm install
# Expose the port the app runs on
EXPOSE 5173
# Start the React app
CMD ["npm", "run", "dev", "--","--host"]