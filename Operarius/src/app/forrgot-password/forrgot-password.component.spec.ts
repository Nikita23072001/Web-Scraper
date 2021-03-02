import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ForrgotPasswordComponent } from './forrgot-password.component';

describe('ForrgotPasswordComponent', () => {
  let component: ForrgotPasswordComponent;
  let fixture: ComponentFixture<ForrgotPasswordComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ForrgotPasswordComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ForrgotPasswordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
