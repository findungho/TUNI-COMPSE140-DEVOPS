# start by pulling the node image
FROM node:14

# switch working directory
WORKDIR /IMED

# copy every content from the local file to the image
COPY ./ ./

# Expose port
EXPOSE 8002

# Install packages
RUN npm install

CMD [ "npm", "start" ]