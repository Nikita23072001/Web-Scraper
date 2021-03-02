import { Component, OnInit } from '@angular/core';
import { INgxChatUiMessagePartner, INgxChatUiMessage, INgxChatUiState, INgxChatUiMessageType, INgxChatUiMessagePayload } from 'ngx-chat-ui';
@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {
  partners: INgxChatUiMessagePartner[] = [];
  messages: {
    [chatKey: string]: INgxChatUiMessage[]
  } = {
    demoSelect: [],
    demoText: [],
    demoList: [],
    demoAutocomplete: [],
    demoUpload: []
  };
  state: {
    [chatKey: string]: INgxChatUiState
  } = {
    demoSelect: {},
    demoText: {},
    demoList: {},
    demoAutocomplete: {},
    demoUpload: {}
  };
  callbacks: {
    // tslint:disable-next-line:ban-types
    [chatKey: string]: { [name: string]: Function }
  } = {
    demoAutocomplete: {
      autocomplete: this.autocompleteTags.bind(this),
    },
    demoUpload: {
      upload: this.uploadFiles.bind(this),
    }
  };

  // tslint:disable-next-line:use-life-cycle-interface
  ngOnInit() {
    this.partners = this.partners.concat([
      {
        messagePartnerId: 'me',
        firstName: 'Sergey',
        lastName: 'Kalaus'
      },
      {
        messagePartnerId: 'it',
        // tslint:disable-next-line:max-line-length
        avatar: 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4QBmRXhpZgAATU0AKgAAAAgABAEaAAUAAAABAAAAPgEbAAUAAAABAAAARgEoAAMAAAABAAIAAAExAAIAAAAQAAAATgAAAAAAAABgAAAAAQAAAGAAAAABcGFpbnQubmV0IDQuMS42AP/bAEMABQQEBAQDBQQEBAYFBQYIDQgIBwcIEAsMCQ0TEBQTEhASEhQXHRkUFhwWEhIaIxocHh8hISEUGSQnJCAmHSAhIP/bAEMBBQYGCAcIDwgIDyAVEhUgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIP/AABEIABgAGAMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APsW7uoLGzlu7l9kUS7mP+e9YH/CbaH9hW43y+aW2m2Cgyr7kZxjHOc/rxVXx88kej2hVm8t7gRuqgnPyswJ5xgFR2P4V5nFb3yyBZL7fEgXafLAd8DneenPXgD8K8HH5jPD1fZwS26nqYXBxqw55dz3mORJYkljYMjgMrDoQehorjvh7eXkujXFjeytK9rIAjnuhHA644wRgAcAcUV7FCqq1NVI9Tz6kHTm4PodVe2NrqFqba8iEkZ5weoPqPQ1zf8Awgun+du+13Hl/wB3jP54/pRRUVcLRrNOpG7Kp16lNWg7HSWVja6darbWkQjjHPuT6k96KKK3jFRXLFWRk227s//Z'
      }
    ]);

    this.messages.demoSelect = this.messages.demoSelect.concat([
      {
        date: new Date(),
        messagePartnerId: 'me',
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Hello'
        }
      },
      {
        date: new Date(),
        messageId: '1',
        messagePartnerId: 'it',
        isIncoming: true,
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Wanna play?'
        },
        action: {
          type: INgxChatUiMessageType.select,
          items: [
            {
              icon: '👌',
              id: 0,
              className: 'ngx-chat-ui-action-select-item-cta'
            },
            {
              text: 'No',
              id: 1
            }
          ]
        }
      },
    ]);

    this.messages.demoText = this.messages.demoText.concat([
      {
        date: new Date(),
        messagePartnerId: 'me',
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Hello'
        }
      },
      {
        date: new Date(),
        messageId: '2',
        messagePartnerId: 'it',
        isIncoming: true,
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Wanna play?'
        },
        action: {
          type: INgxChatUiMessageType.text
        }
      },
    ]);

    this.messages.demoList = this.messages.demoList.concat([
      {
        date: new Date(),
        messagePartnerId: 'me',
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Hello'
        }
      },
      {
        date: new Date(),
        messageId: '2',
        messagePartnerId: 'it',
        isIncoming: true,
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Wanna play?'
        },
        action: {
          type: INgxChatUiMessageType.select,
          className: 'ngx-chat-ui-action-select-list',
          items: [
            {
              text: 'Yes',
              id: 0,
              className: 'ngx-chat-ui-action-select-item-cta'
            },
            {
              text: 'No',
              id: 1
            }
          ]
        }
      },
    ]);

    this.messages.demoAutocomplete = this.messages.demoAutocomplete.concat([
      {
        date: new Date(),
        messagePartnerId: 'me',
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Hello'
        }
      },
      {
        date: new Date(),
        messagePartnerId: 'it',
        isIncoming: true,
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Wanna play?'
        },
        action: {
          type: INgxChatUiMessageType.autocomplete,
          callback: 'autocomplete',
        }
      },
    ]);

    this.messages.demoUpload = this.messages.demoUpload.concat([
      {
        date: new Date(),
        messagePartnerId: 'me',
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Hello'
        }
      },
      {
        date: new Date(),
        messagePartnerId: 'it',
        isIncoming: true,
        payload: {
          type: INgxChatUiMessageType.text,
          value: 'Wanna play?'
        },
        action: {
          type: INgxChatUiMessageType.upload,
          callback: 'upload',
        }
      },
    ]);
  }

  onResponse(chatKey: string, payload: INgxChatUiMessagePayload) {
    setTimeout(() => {
      this.messages[chatKey] = this.messages[chatKey].concat([
        {
          date: new Date(),
          messagePartnerId: 'me',
          payload
        }
      ]);
    });
  }

  // tslint:disable-next-line:ban-types
  autocompleteTags(query: string, callback: Function) {
    callback([
      '#aabbccdd',
      '#eeffgghh',
      '#iijjkkll',
      '#mmnnoopp',
      '#qqrrsstt',
      '#uuvvwwxx',
      '#yyzz',
    ]);
  }

  // tslint:disable-next-line:ban-types
  uploadFiles(data: any, callback: Function) {
    callback({
      name: 'Test.jpg',
      url: 'https://via.placeholder.com/150',
    });
  }

}
