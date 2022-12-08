# start by pulling the node image
FROM node:14

# switch working directory
WORKDIR /ORIG

# copy every content from the local file to the image
COPY ./ ./

# Expose port
EXPOSE 8001

# Install packages
RUN npm install

CMD [ "npm", "start" ]