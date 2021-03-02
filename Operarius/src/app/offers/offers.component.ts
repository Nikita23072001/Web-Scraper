import { RouterModule, Router } from '@angular/router';
import { OfferService } from 'src/app/shared/offer.service';
import { offer } from './Offer';
import { Component, OnInit, Renderer } from '@angular/core';
import { Offer } from '../shared/offer.model';

@Component({
  selector: 'app-offers',
  templateUrl: './offers.component.html',
  styleUrls: ['./offers.component.css']
})
export class OffersComponent implements OnInit {
  list: Offer[];
  dtOptions: DataTables.Settings = {};
  constructor(private service: OfferService, private renderer: Renderer, private router: Router) {
  }

  ngOnInit() {
    this.service.getOffers().subscribe(actionArray => {
    this.list = actionArray.map(item => {
      return {
        id: item.payload.doc.id,
        ...item.payload.doc.data() } as Offer;
    // tslint:disable-next-line:semicolon
    })
    });

    this.dtOptions = {
      ajax: 'data/data.json',
      columns: [{
        title: 'ID',
        data: 'id'
      }, {
        title: 'First name',
        data: 'firstName'
      }, {
        title: 'Last name',
        data: 'lastName'
      }, {
        title: 'Action',
        render(data: any, type: any, full: any) {
          return 'View';
        }
      }]
    };
  }

  // tslint:disable-next-line:use-life-cycle-interface


 // onSelect(Offer: offer): void {
   // this.selectedOffer = Offer;
 // }
}
